# Recette FoodEatUp V2 — familles site / caisse / fidélité / avis — 2026-07-15

Établissement de test : **`establishment_id = 2` (« gosushi », démo)** — **jamais le 26**.

## Validation live (lecture) — FAIT

Les 4 nouvelles familles répondent en direct avec les schémas réintrospectés
(2026-07-15), sur le serveur reconnecté (164 outils) :

| Famille | Appel (lecture) | Résultat observé |
|---|---|---|
| Site vitrine | `get_site_status(2)` | `published:false`, url `foodeatup.com/shop/gosushi`, `pages: {published:0, draft:0}`, `custom_domain:null` |
| Fidélité | `get_loyalty_program(2)` | `id:2`, `active:false`, `earn_mode:per_euro`, `earn_rate:1.00` |
| Caisse (POS) | `get_pos_session(2)` | `open:false` — « Aucune session de caisse ouverte. » |
| Avis | `list_reviews(2)` | `[]` (aucun avis sur le démo) |

→ **Schémas confirmés, connexion et périmètre (démo gosushi) validés.** Le démo est
**vierge** (0 page, fidélité inactive, pas de caisse ouverte, pas d'avis).

## Recette écriture — runbook supervisé (à rejouer avec Mo, établissement 2)

Les écritures sont **outward-facing** (publication, encaissement, réponse publique) :
elles se jouent **en supervision**, une action **confirmée** par famille. Le démo étant
vierge, certaines nécessitent une donnée de départ (notée ci-dessous).

1. **Site** — `add_site_page(2, type="about")` (créée **en brouillon**) → `get_site_status(2)`
   (draft = 1). Option : `toggle_site_page` puis `publish_site(2, confirm=true)` **après
   récap** — ou laisser en brouillon pour ne rien exposer. Ne **jamais** `confirm:true`
   d'office.
2. **Fidélité** — `upsert_loyalty_reward(2, kind="perk", label="Café offert (test)",
   points_cost=50)` → `list_loyalty_rewards(2)` (récompense présente). `validate_redemption`
   **non joué** : aucun bon émis sur le démo (à rejouer quand un bon existe).
3. **Caisse** — `open_pos_session(2, opening_float=50, operator_id=<employé caisse>)` →
   `get_pos_report(2)` (**rapport X**). **PAS** de `record_pos_payment` (argent réel) ni de
   `close_pos_session` **Z** en recette. Simuler à blanc si des données de prod
   apparaissent.
4. **Avis** — `list_reviews(2)` = vide sur le démo → `moderate_review` / `reply_review`
   (**réponse en brouillon validée avant**) **à rejouer** quand un avis test existe.

## Écarts

- Le démo `gosushi` est **vierge** : les volets **avis** et **validation de bon** n'ont
  pas de donnée de départ → **validés par lecture**, écriture à rejouer supervisée.
- Aucune écriture n'a été déclenchée automatiquement (règle : confirmation humaine avant
  toute action outward-facing sur un établissement réel).
