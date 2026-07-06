---
name: carte-digitale
description: Utiliser quand l'utilisateur parle de carte de visite digitale, de carte NFC, de page de carte ou d'ajouter un lien à une carte. Crée la carte, lui assigne un template avec QR code et édite ses pages et liens.
---

# Carte digitale

## Workflow

1. **Créer la carte** — `add_digital_card`. TOUS les champs sont requis :
   `card_name`, `owner_first_name`, `owner_last_name`, `owner_email`,
   `owner_phone` (chiffres uniquement, sans espaces ni « + »), `other_info`.
   Demander les informations manquantes avant l'appel.
2. **Assigner un template** — lister avec `list_card_templates` (`type` = visite |
   nfc, `search` mot-clé), puis `assign_card_template` (`template_id`, `card_id`).
   - RÈGLE : le template choisi doit inclure un QR code, pour les cartes visite
     comme NFC. Si aucun template avec QR code ne correspond, le signaler à
     l'utilisateur au lieu d'assigner un template sans QR code.
3. **Éditer les pages** — retrouver les pages avec `list_card_page`, puis
   `edit_card_page` (`page_id` requis ; `text` en HTML avec styles CSS inline —
   couleurs, tailles, décorations dans les éléments eux-mêmes —, `background`
   couleur de fond, `image_url` URL publique, `width`/`height` en pixels).
4. **Ajouter des liens** — `add_card_page_link` (`page_id`, `link_url` en http/https,
   `name` requis ; `image_url` publique optionnelle pour l'icône). Vérifier que
   chaque URL est valide et complète (avec https://).

## Garde-fous

- Respecter la charte de marque (couleurs, logo) dans `edit_card_page` — voir le
  skill contenu-conforme-marque (`get_brand`).
- Suppression d'une carte (`delete_digital_card`) ou d'un lien
  (`delete_card_page_link`) : confirmation explicite obligatoire.
- Récapituler en fin de workflow : carte créée, template assigné (avec QR code),
  pages éditées, liens ajoutés.
