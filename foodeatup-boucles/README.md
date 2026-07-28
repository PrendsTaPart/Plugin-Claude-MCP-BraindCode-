# foodeatup-boucles

Pilotage d'un restaurant FoodEatUp **par les 8 boucles du livre blanc**, en
complément (pas en remplacement) du plugin `foodeatup` : chaque boucle a son
skill de diagnostic, le croisement gestion × vente a le sien, et trois hooks
verrouillent les écritures sensibles.

## Ce que fait le plugin

- **8 skills de boucle** (`boucle-1-configuration` … `boucle-8-comptabilite`) :
  état de santé d'une boucle, trous détectés, actions proposées — l'opération
  fine reste dans les skills spécialisés du plugin `foodeatup`.
- **1 skill de croisement** (`croisement-service`) : le seul qui lit les deux
  familles de boucles en même temps et détecte les contradictions (plat en
  campagne / stock bas, production sans demande, marge négative en promo,
  fidélité éteinte / récompenses actives) — et qui répond « données
  insuffisantes » sous les seuils d'échantillon au lieu de recommander quand même.
- **1 skill d'auto-formation** (`decouvrir-le-plugin`) : carte de la
  marketplace générée depuis le dépôt réel (`scripts/generer-carte-boucles.py`).
- **4 commands** : `/boucles`, `/boucle <n>`, `/croisement`, `/sante-donnees`.
- **3 subagents** : `direction` (lecture seule), `exploitation` (écritures du
  service uniquement), `marketing` (brouillons oui, lancement jamais) — les
  permissions sont déclarées explicitement dans leur frontmatter `tools`.
- **3 hooks** :
  - `PreToolUse` : garde-fou destructif **fail-closed** — liste
    `hooks/scripts/outils-destructifs.txt`, confirmation humaine forcée, champs
    `confirm`/`confirmed` du modèle volontairement ignorés ;
  - `SessionStart` : contexte établissement (fidélité active ?, volumétrie
    clients, campagnes, alertes HACCP) chargé avant tout échange ;
  - `PostToolUse` : journal des écritures MCP dans
    `.claude/logs/ecritures-<date>.jsonl` (secrets masqués, lectures exclues).

## Prérequis

- Serveur **MCP FoodEatUp connecté** (obligatoire — le plugin ne fait rien sans).
- Serveur MCP RapidoCRM connecté (optionnel : volets pipeline et campagnes CRM).
- Python 3 disponible (hooks).

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install foodeatup-boucles@rapido
```

## Les 8 boucles

| n° | Boucle | Famille | Skill |
|---|---|---|---|
| ① | Configuration | gestion | `boucle-1-configuration` |
| ② | Équipe | gestion | `boucle-2-equipe` |
| ③ | Stock / Production | gestion | `boucle-3-stock-production` |
| ④ | HACCP | gestion | `boucle-4-haccp` |
| ⑤ | E-commerce / Vente | vente | `boucle-5-ecommerce` |
| ⑥ | Communication | vente | `boucle-6-communication` |
| ⑦ | Fidélité | vente | `boucle-7-fidelite` |
| ⑧ | Comptabilité | vente | `boucle-8-comptabilite` |

Le croisement du 8 — le service, traversé par la commande, l'encaissement, la
carte et la marge — est couvert par `croisement-service`.

La cartographie complète outils MCP × boucles vit dans
`docs/boucles-vs-outils.md` (dépôt de la marketplace) ; les limites du moteur
fidélité/jeux dans `docs/couverture-fidelite-jeux.md`.
