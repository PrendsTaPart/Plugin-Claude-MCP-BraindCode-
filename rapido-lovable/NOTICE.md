# NOTICE — rapido-lovable

Le **kit connecteur MCP** (`reference/kit-connecteur-mcp/`) et les règles de stack /
gate sécurité **s'inspirent de** dépôts open source. On **francise/réimplémente des
méthodes** ; aucun corps de texte ni code source n'est redistribué verbatim.

## Sources (frameworks adaptés, non redistribués)

| Dépôt | Licence | Ce qui est repris |
|---|---|---|
| [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | **CC0-1.0** (domaine public) | Sélection francisée de règles de stack (React/TS/Tailwind/shadcn/Supabase) → `reference/regles-stack-lovable.md` |
| [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) | **Apache-2.0** | Checklist sécurité **adaptée et modifiée** (spécialisée « agent + clés MCP ») → `reference/gate-securite.md` |
| [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | MIT | Pattern **spec-driven** (specs avant prompts) → ossature de `mvp-lovable` (LV3) |
| [AndreAlmeidaDC/lovable-prompt-builder](https://github.com/AndreAlmeidaDC/lovable-prompt-builder) | MIT | Logique **intake → prompts atomiques → feedback** → `connecteur-mcp-lovable` / `mvp-lovable` |

## Modifications (exigence Apache-2.0 pour VibeSec)

`reference/gate-securite.md` est une **œuvre dérivée modifiée** de VibeSec-Skill : la
checklist a été traduite en français, condensée, et **réorganisée autour du cas d'usage
« site Lovable embarquant un agent connecté à un MCP »** (ajout des points scope
multi-tenant, écritures confirmées, secrets MCP hors bundle). Le texte original n'est pas
reproduit.

## Pattern de référence (interne)

Le template d'edge function du kit **canonise du code de production BraindCode**
(`academyrapido:execute-prompt`, documenté dans `docs/REFERENCE-AGENT-LOVABLE.md`) — pas
un tiers.

## Exclusions

- `karozi/Awesome-Vibecoding` (**sans licence**) : **benchmark seul, jamais fusionné**.
- Aucune clé, aucune donnée client dans le dépôt. Les secrets vivent en env Lovable/Supabase.
