# Installation du plugin rapido-direction

Ce plugin est GÉNÉRALISTE : chaque utilisateur connecte SON PROPRE compte
Google (Gmail, Calendar, Drive). Les URLs des serveurs MCP Google sont
publiques et identiques pour tous — c'est l'AUTHENTIFICATION OAuth qui est
individuelle : au premier usage, chacun autorise son compte.

## 1. Connecter son compte Google

- **Claude Code** : au premier appel d'un outil Gmail/Calendar/Drive, le flux
  OAuth s'ouvre — connectez le compte Google PROFESSIONNEL que le plugin doit
  utiliser (`/mcp` liste les serveurs et leur état d'authentification).
- **claude.ai / Desktop** : Paramètres → Connecteurs → activer Gmail,
  Google Calendar et Google Drive avec votre compte.
- Vérifiez les URLs des serveurs dans `.mcp.json` contre la documentation
  officielle des connecteurs Google MCP si la connexion échoue (elles peuvent
  évoluer) — les corriger dans le plugin le cas échéant.

## 2. Vérification

Demandez : « cherche mes 3 derniers fils de mails » — `search_threads` doit
répondre après l'autorisation OAuth.

## 3. Dégradation propre

Si les outils Gmail/Calendar/Drive sont ABSENTS de la session (compte non
connecté, connecteur désactivé), les skills du plugin l'expliquent et
DÉGRADENT proprement : la `journee-du-dirigeant` se fait sans le volet emails
(agenda CRM + FoodEatUp + alertes n8n restent), le `coffre-documents` renvoie
vers ce README, etc. Aucun skill n'échoue sèchement.

## Rappels

- Jamais de boîte mail, d'agenda ou de Drive « particulier » codé dans les
  skills : toujours « le compte connecté ».
- Gmail via MCP ne fait QUE des brouillons — Claude rédige, VOUS envoyez.
- `N8N_MCP_URL` (instance n8n du client) : voir
  `rapido-n8n/README-installation.md` — optionnelle, le plugin dégrade sans.
- Fuseau horaire : renseigné dans `rapido-kb/entreprise.md` à l'onboarding.
