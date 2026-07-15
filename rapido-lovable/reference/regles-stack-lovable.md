# Règles de stack Lovable (à injecter dans chaque prompt généré)

**Kit v1 · 2026-07-15.** Sélection francisée des bonnes pratiques pour la stack Lovable
(**React + TypeScript + Tailwind + shadcn/ui + Supabase**). À insérer en tête de tout
prompt Lovable (connecteur, MVP) pour un résultat homogène. Source : `awesome-cursorrules`
(CC0-1.0, domaine public — crédit en pied).

## Style & structure

- **TypeScript partout**, types explicites aux frontières (props, retours d'API, payloads
  edge). Éviter `any` ; préférer des types/interfaces nommés.
- Composants **fonctionnels** + hooks ; un composant = une responsabilité. Fichiers
  courts, imports ordonnés.
- Nommage : composants `PascalCase`, hooks `useXxx`, variables/handlers `camelCase`
  (`handleSubmit`, `onConfirm`). Dossiers en `kebab-case`.

## UI & styling

- **Tailwind** pour tout le style (pas de CSS ad hoc) ; **shadcn/ui** pour les primitives
  (Button, Card, Dialog, Input…). Respecter la charte (couleurs/typos) via les tokens du
  design system, pas de valeurs en dur.
- **Responsive** (mobile-first) et **accessibilité** : labels, rôles ARIA, focus visible,
  contraste suffisant.

## Données & Supabase

- Accès données via le **client Supabase** ; jamais de secret côté navigateur.
- Toute logique sensible (clés, appels externes, MCP, IA) en **edge function** — le front
  n'appelle que ses propres endpoints.
- Validation **serveur** systématique des entrées (jamais faire confiance au front).

## Performance & qualité

- Charger à la demande (code-splitting, `lazy`), mémoïser ce qui doit l'être, éviter les
  re-renders inutiles.
- Gérer explicitement les états **chargement / erreur / vide** de chaque écran.
- Pas de code mort ni de `console.log` en production ; messages d'erreur clairs et
  actionnables.

## À proscrire

- Clés/URLs/API en dur dans le code ou le bundle → **secrets Lovable/Supabase**.
- Appels directs `api.anthropic.com` ou MCP depuis le navigateur → **edge function**.
- Reporter la sécurité « à plus tard » : le gate (`gate-securite.md`) est **bloquant**.

---
*Adapté de [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)
(CC0-1.0). Francisé et condensé pour la stack Lovable — voir `NOTICE.md`.*
