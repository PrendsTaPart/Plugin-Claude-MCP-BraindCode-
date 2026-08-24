const DEFAULT_PROTECTED_SERVERS = Object.freeze([
  "analytics",
  "canva",
  "dataforseo",
  "elevenlabs",
  "facebook-ads",
  "foodeatup",
  "gmail",
  "google-ads",
  "google-calendar",
  "google-drive",
  "gsc",
  "huggsfield",
  "hyperframes",
  "lovable",
  "n8n",
  "rapidocms",
  "rapidocrm",
  "rapidorh",
  "stripe",
  "tiktok-ads",
]);

const PAID_SERVERS = Object.freeze([
  "dataforseo",
  "elevenlabs",
  "huggsfield",
  "hyperframes",
  "lovable",
]);

const READ_ONLY_PREFIXES = Object.freeze([
  "analyze",
  "audit",
  "calculate",
  "check",
  "count",
  "describe",
  "find",
  "get",
  "health",
  "inspect",
  "list",
  "lookup",
  "preview",
  "read",
  "report",
  "search",
  "stats",
  "status",
  "summarize",
  "validate",
  "view",
]);

const CRITICAL_PREFIXES = Object.freeze([
  "activate",
  "cancel",
  "charge",
  "close",
  "delete",
  "disable",
  "launch",
  "pay",
  "publish",
  "refund",
  "remove",
  "send",
  "spend",
  "submit",
]);

const WRITE_PREFIXES = Object.freeze([
  "add",
  "approve",
  "archive",
  "assign",
  "create",
  "edit",
  "enable",
  "import",
  "invite",
  "merge",
  "moderate",
  "move",
  "record",
  "reject",
  "reply",
  "schedule",
  "set",
  "sync",
  "update",
  "upload",
  "write",
]);

const SENSITIVE_KEY = /(?:^|_)(?:api_?key|authorization|bearer|credential|password|private_?key|secret|token)(?:$|_)/i;

function normalizeVerb(tool) {
  return tool.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "");
}

function startsWithAny(value, prefixes) {
  return prefixes.some((prefix) => value === prefix || value.startsWith(`${prefix}_`));
}

function containsAnyToken(value, tokens) {
  const valueTokens = new Set(value.split("_").filter(Boolean));
  return tokens.some((token) => valueTokens.has(token));
}

export function parseMcpToolName(toolName) {
  if (typeof toolName !== "string") return null;
  const parts = toolName.split("__");
  if (parts.length < 2 || parts.some((part) => part.length === 0)) return null;
  const hasNamespace = parts.length >= 3 && ["bundle-mcp", "mcp"].includes(parts[0]);
  const serverIndex = hasNamespace ? 1 : 0;
  if (parts.length <= serverIndex + 1) return null;
  return {
    server: parts[serverIndex].toLowerCase(),
    tool: parts.slice(serverIndex + 1).join("__"),
  };
}

export function containsSensitiveInput(value, depth = 0) {
  if (depth > 8 || value === null || typeof value !== "object") return false;
  if (Array.isArray(value)) {
    return value.some((item) => containsSensitiveInput(item, depth + 1));
  }
  return Object.entries(value).some(([key, child]) => {
    if (SENSITIVE_KEY.test(key) && child !== null && child !== "") return true;
    return containsSensitiveInput(child, depth + 1);
  });
}

export function mustBlockRequester(requester) {
  return requester !== null && requester !== undefined && requester.senderIsOwner !== true;
}

export function classifyToolCall(
  toolName,
  input,
  protectedServers = DEFAULT_PROTECTED_SERVERS,
) {
  const parsed = parseMcpToolName(toolName);
  if (!parsed || !protectedServers.includes(parsed.server)) {
    return { action: "ignore", reason: "outside_rapido_mcp" };
  }

  const normalizedTool = normalizeVerb(parsed.tool);
  if (containsSensitiveInput(input)) {
    return {
      action: "block",
      severity: "critical",
      reason: "sensitive_input",
      server: parsed.server,
      tool: parsed.tool,
    };
  }
  if (PAID_SERVERS.includes(parsed.server)) {
    return {
      action: "approve",
      severity: "critical",
      reason: "paid_service",
      server: parsed.server,
      tool: parsed.tool,
    };
  }
  if (containsAnyToken(normalizedTool, CRITICAL_PREFIXES)) {
    return {
      action: "approve",
      severity: "critical",
      reason: "critical_write",
      server: parsed.server,
      tool: parsed.tool,
    };
  }
  if (startsWithAny(normalizedTool, READ_ONLY_PREFIXES)) {
    return {
      action: "allow",
      reason: "recognized_read",
      server: parsed.server,
      tool: parsed.tool,
    };
  }
  if (startsWithAny(normalizedTool, WRITE_PREFIXES)) {
    return {
      action: "approve",
      severity: "warning",
      reason: "write",
      server: parsed.server,
      tool: parsed.tool,
    };
  }
  return {
    action: "approve",
    severity: "warning",
    reason: "unknown_tool",
    server: parsed.server,
    tool: parsed.tool,
  };
}

export { DEFAULT_PROTECTED_SERVERS };
