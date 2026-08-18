[CmdletBinding()]
param(
    [ValidateSet("core", "all")]
    [string]$Scope = "core",

    [string]$RepoRoot = "",

    [switch]$ConfigureWhatsApp,

    [string]$WhatsAppNumber = "",

    [switch]$SetOpenAIModel,

    [switch]$StartOAuthLogin,

    [switch]$SkipGatewayRestart,

    [switch]$DryRun,

    [switch]$SelfTest,

    [ValidateRange(1, 100)]
    [int]$MinimumFreeGb = 2
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $RepoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "..\.."))
} else {
    $RepoRoot = [IO.Path]::GetFullPath($RepoRoot)
}

function Format-Command {
    param([string]$Command, [string[]]$Arguments)
    $quoted = $Arguments | ForEach-Object {
        if ($_ -match '[\s"]') { '"' + ($_ -replace '"', '\"') + '"' } else { $_ }
    }
    $parts = @($Command) + @($quoted)
    return ($parts -join " ").Trim()
}

function Get-GuardInstallArguments {
    param([Parameter(Mandatory = $true)][string]$PluginPath)
    @("plugins", "install", "--link", $PluginPath)
}

function ConvertTo-NativeJsonArgument {
    param([Parameter(Mandatory = $true)][string]$Json)
    if ($PSVersionTable.PSEdition -eq "Desktop") {
        return $Json.Replace('"', '\"')
    }
    return $Json
}

if ($SelfTest) {
    $guardArguments = @(Get-GuardInstallArguments -PluginPath "C:\Rapido Guard")
    if ($guardArguments -contains "--force") {
        throw "Linked plugin installs must not use --force."
    }
    $sample = Format-Command "openclaw" $guardArguments
    $expected = 'openclaw plugins install --link "C:\Rapido Guard"'
    if ($sample -ne $expected) {
        throw "Format-Command self-test failed: $sample"
    }
    $rawJson = '{"url":"https://example.invalid/api/mcp","auth":"oauth"}'
    $nativeJson = ConvertTo-NativeJsonArgument -Json $rawJson
    $expectedNativeJson = if ($PSVersionTable.PSEdition -eq "Desktop") {
        '{\"url\":\"https://example.invalid/api/mcp\",\"auth\":\"oauth\"}'
    } else {
        $rawJson
    }
    if ($nativeJson -ne $expectedNativeJson) {
        throw "Native JSON escaping self-test failed: $nativeJson"
    }
    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        throw "Node.js is required for the native JSON round-trip self-test."
    }
    $roundTripJson = & node -e 'process.stdout.write(process.argv[1])' $nativeJson
    if ($LASTEXITCODE -ne 0 -or $roundTripJson -ne $rawJson) {
        throw "Native JSON round-trip self-test failed: $roundTripJson"
    }
    $nonAsciiBytes = @([IO.File]::ReadAllBytes($PSCommandPath) | Where-Object { $_ -gt 127 })
    if ($nonAsciiBytes.Count -gt 0) {
        throw "The PowerShell installer must remain ASCII-compatible with Windows PowerShell 5.1."
    }
    Write-Host "PowerShell installer self-test OK"
    exit 0
}

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)][string]$Command,
        [Parameter(Mandatory = $true)][string[]]$Arguments
    )
    Write-Host ("> " + (Format-Command $Command $Arguments)) -ForegroundColor DarkGray
    if ($DryRun) { return }
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Commande en echec ($LASTEXITCODE): $(Format-Command $Command $Arguments)"
    }
}

function Find-Python {
    if (Get-Command python -ErrorAction SilentlyContinue) {
        return @{ Command = "python"; Prefix = @() }
    }
    if (Get-Command py -ErrorAction SilentlyContinue) {
        return @{ Command = "py"; Prefix = @("-3") }
    }
    throw "Python 3 est requis pour convertir les declarations MCP."
}

function Assert-SupportedNode {
    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        throw "Node.js est introuvable. OpenClaw exige Node 22.22.3+, 24.15+ ou 25.9+."
    }
    $rawVersion = (& node --version).Trim().TrimStart('v')
    try {
        $nodeVersion = [version]($rawVersion -replace '-.*$', '')
    } catch {
        throw "Version Node.js illisible : $rawVersion"
    }
    $supported = (
        ($nodeVersion.Major -eq 22 -and $nodeVersion -ge [version]"22.22.3") -or
        ($nodeVersion.Major -eq 24 -and $nodeVersion -ge [version]"24.15.0") -or
        ($nodeVersion.Major -eq 25 -and $nodeVersion -ge [version]"25.9.0")
    )
    if (-not $supported) {
        throw "Node.js $nodeVersion non supporte. Installez Node 22.22.3+, 24.15+ ou 25.9+, puis ouvrez un nouveau terminal."
    }
    Write-Host "Node.js supporte : v$nodeVersion" -ForegroundColor Cyan
}

if (-not (Test-Path (Join-Path $RepoRoot ".claude-plugin\marketplace.json"))) {
    throw "Marketplace Rapido introuvable dans : $RepoRoot"
}
if (-not (Get-Command openclaw -ErrorAction SilentlyContinue)) {
    throw "La commande openclaw est introuvable. Installez ou corrigez le PATH avant de continuer."
}
Assert-SupportedNode

$driveRoot = [IO.Path]::GetPathRoot($RepoRoot)
if ($driveRoot -and $driveRoot.Length -ge 2 -and $driveRoot[1] -eq ':') {
    $driveName = $driveRoot.Substring(0, 1)
    $drive = Get-PSDrive -Name $driveName -ErrorAction Stop
    $minimumBytes = [int64]$MinimumFreeGb * 1GB
    if ($drive.Free -lt $minimumBytes) {
        $freeGb = [math]::Round($drive.Free / 1GB, 2)
        throw "Espace disque insuffisant sur $driveName`: $freeGb Go libres; minimum $MinimumFreeGb Go."
    }
}

$marketplace = Get-Content (Join-Path $RepoRoot ".claude-plugin\marketplace.json") -Raw | ConvertFrom-Json
$corePlugins = @("rapido-suite", "rapidocrm", "rapidocms", "rapidorh", "foodeatup")
$plugins = if ($Scope -eq "all") {
    @($marketplace.plugins | ForEach-Object { [string]$_.name })
} else {
    $corePlugins
}

$stateDir = if (-not [string]::IsNullOrWhiteSpace($env:OPENCLAW_STATE_DIR)) {
    $env:OPENCLAW_STATE_DIR
} else {
    Join-Path $env:USERPROFILE ".openclaw"
}
$configPath = Join-Path $stateDir "openclaw.json"
if (Test-Path $configPath) {
    $backupDirectory = Join-Path $stateDir "backups"
    $backupPath = Join-Path $backupDirectory ("openclaw-before-rapido-{0}.json" -f (Get-Date -Format "yyyyMMdd-HHmmss"))
    Write-Host "Sauvegarde locale : $backupPath" -ForegroundColor Cyan
    if (-not $DryRun) {
        New-Item -ItemType Directory -Path $backupDirectory -Force | Out-Null
        Copy-Item -LiteralPath $configPath -Destination $backupPath -Force
    }
}

Write-Host "OpenClaw detecte :" -ForegroundColor Cyan
Invoke-Checked "openclaw" @("--version")
$guardPath = Join-Path $RepoRoot "openclaw-rapido-guard"
Write-Host "Installation et preuve runtime du garde-fou avant les MCP" -ForegroundColor Cyan
$guardInstallArguments = @(Get-GuardInstallArguments -PluginPath $guardPath)
Invoke-Checked "openclaw" $guardInstallArguments
Invoke-Checked "openclaw" @("plugins", "enable", "rapido-guard")
Invoke-Checked "openclaw" @("gateway", "restart")
Invoke-Checked "openclaw" @("gateway", "status", "--deep", "--require-rpc")
Invoke-Checked "openclaw" @("plugins", "inspect", "rapido-guard", "--runtime", "--json")

Write-Host "Installation de $($plugins.Count) plugin(s) Rapido depuis $RepoRoot" -ForegroundColor Cyan
foreach ($plugin in $plugins) {
    Invoke-Checked "openclaw" @(
        "plugins", "install", $plugin,
        "--marketplace", $RepoRoot,
        "--force"
    )
}

if ($Scope -eq "all") {
    $python = Find-Python
    $generator = Join-Path $RepoRoot "scripts\openclaw\generate_mcp_config.py"
    $generatorArguments = @($python.Prefix) + @($generator, "--repo", $RepoRoot)
    foreach ($plugin in $plugins) {
        $generatorArguments += @("--plugin", $plugin)
    }
    $generatorArguments += @("--include-satellites", "--expand-url-env")
    $generatedText = & $python.Command @generatorArguments | Out-String
    if ($LASTEXITCODE -ne 0) {
        throw "La generation de la configuration MCP a echoue."
    }
} else {
    $coreConfigPath = Join-Path $RepoRoot "scripts\openclaw\core-mcp.json"
    $generatedText = Get-Content $coreConfigPath -Raw
}
$generated = $generatedText | ConvertFrom-Json
$serverProperties = @($generated.servers.PSObject.Properties)

Write-Host "Enregistrement de $($serverProperties.Count) serveur(s) MCP" -ForegroundColor Cyan
foreach ($property in $serverProperties) {
    $serverJson = $property.Value | ConvertTo-Json -Compress -Depth 20
    $serverJsonArgument = ConvertTo-NativeJsonArgument -Json $serverJson
    Invoke-Checked "openclaw" @("mcp", "set", $property.Name, $serverJsonArgument)
}

foreach ($skipped in @($generated.skipped)) {
    $variables = @($skipped.variables) -join ", "
    Write-Warning "MCP '$($skipped.server)' ignore : variable(s) d'URL absente(s) ou expansion non demandee ($variables)."
}

if ($SetOpenAIModel) {
    Write-Host "> openclaw models list --provider openai" -ForegroundColor DarkGray
    $modelListText = & openclaw models list --provider openai | Out-String
    if ($LASTEXITCODE -ne 0) {
        throw "Impossible de lire le catalogue OpenAI de ce compte."
    }
    Write-Host $modelListText.TrimEnd()
    if ($modelListText -notmatch [regex]::Escape("openai/gpt-5.6-sol")) {
        throw "Le compte ne confirme pas l'acces a openai/gpt-5.6-sol. Choisissez explicitement un modele disponible."
    }
    $modelJson = ConvertTo-NativeJsonArgument -Json (
        "openai/gpt-5.6-sol" | ConvertTo-Json -Compress
    )
    Invoke-Checked "openclaw" @(
        "config", "set", "agents.defaults.model.primary", $modelJson, "--strict-json"
    )
}

if ($ConfigureWhatsApp) {
    $phoneDigits = $WhatsAppNumber -replace '^\+', ''
    if ($phoneDigits -notmatch '^[1-9][0-9]{7,14}$') {
        throw "-WhatsAppNumber doit etre au format E.164, par exemple +216XXXXXXXX."
    }
    $normalizedPhone = "+$phoneDigits"
    $policyJson = ConvertTo-NativeJsonArgument -Json (
        "allowlist" | ConvertTo-Json -Compress
    )
    $allowFromJson = ConvertTo-NativeJsonArgument -Json (
        @($normalizedPhone) | ConvertTo-Json -Compress
    )
    Invoke-Checked "openclaw" @(
        "config", "set", "channels.whatsapp.dmPolicy", $policyJson, "--strict-json"
    )
    Invoke-Checked "openclaw" @(
        "config", "set", "channels.whatsapp.allowFrom", $allowFromJson, "--strict-json"
    )
    Invoke-Checked "openclaw" @(
        "config", "set", "channels.whatsapp.selfChatMode", "true", "--strict-json"
    )
}

if ($StartOAuthLogin) {
    foreach ($serverName in @($serverProperties.Name)) {
        $serverDefinition = $generated.servers.PSObject.Properties[$serverName].Value
        $authProperty = $serverDefinition.PSObject.Properties["auth"]
        if ($null -ne $authProperty -and $authProperty.Value -eq "oauth") {
            Invoke-Checked "openclaw" @("mcp", "login", $serverName)
        }
    }
}

Invoke-Checked "openclaw" @("plugins", "doctor")
Invoke-Checked "openclaw" @("mcp", "doctor", "--probe")
Invoke-Checked "openclaw" @("models", "status")
Invoke-Checked "openclaw" @("channels", "status", "--probe")

if (-not $SkipGatewayRestart) {
    Invoke-Checked "openclaw" @("gateway", "restart")
}
Invoke-Checked "openclaw" @("gateway", "status", "--deep", "--require-rpc")
Invoke-Checked "openclaw" @("plugins", "inspect", "rapido-guard", "--runtime", "--json")

Write-Host ""
Write-Host "Configuration locale terminee." -ForegroundColor Green
if (-not $StartOAuthLogin) {
    Write-Host "Authentification humaine encore requise pour les MCP OAuth :" -ForegroundColor Yellow
    foreach ($serverName in @($serverProperties.Name)) {
        $serverDefinition = $generated.servers.PSObject.Properties[$serverName].Value
        $authProperty = $serverDefinition.PSObject.Properties["auth"]
        if ($null -ne $authProperty -and $authProperty.Value -eq "oauth") {
            Write-Host "  openclaw mcp login $serverName"
        }
    }
}
Write-Host "Test lecture WhatsApp : Liste mes marques RapidoCMS sans rien modifier."
Write-Host "Test garde-fou : Cree un brouillon RapidoCMS nomme TEST-OPENCLAW, sans le publier."
