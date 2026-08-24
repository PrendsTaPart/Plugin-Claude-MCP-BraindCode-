# Rapido Guard pour OpenClaw

Plugin natif OpenClaw qui rétablit les garde-fous des plugins Rapido quand ils
sont utilisés hors de Claude Code. Les anciens `hooks/hooks.json` sont propres à
Claude et ne sont pas exécutés par la couche de compatibilité OpenClaw.

- les outils Rapido reconnus comme lecture passent directement ;
- toute écriture, action destructrice, payante ou inconnue exige une approbation
  `allow-once` ou `deny` ;
- une action inconnue échoue donc fermée ;
- un demandeur de canal identifié mais non vérifié comme propriétaire est bloqué ;
- tout secret placé dans les paramètres d'un outil est bloqué, pas seulement masqué ;
- les valeurs des paramètres ne sont jamais écrites dans les journaux.

Installation depuis la racine de ce dépôt :

```powershell
openclaw plugins install --link .\openclaw-rapido-guard
openclaw plugins enable rapido-guard
openclaw plugins doctor
```

Le plugin protège tous les noms de serveurs déclarés par cette marketplace. Les
services facturés à l'appel (DataForSEO, ElevenLabs, Higgsfield, HyperFrames et
Lovable) demandent aussi une approbation pour leurs opérations de lecture. Le
plugin suppose la convention de nommage OpenClaw Bundle MCP `serveur__outil`.

Tests locaux :

```bash
cd openclaw-rapido-guard
npm test
```
