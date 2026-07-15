# Sync marque — KB ↔ RapidoCMS

Note courte. **La KB (`./rapido-kb/charte-graphique.md`) est la source de
vérité ; la marque RapidoCMS est le miroir d'exécution.** Le contrat détaillé
des outils marque & assets (schémas, `get_brand` renvoie un tableau,
`create_brand` renvoie l'`id`, pas de validation hex serveur, `remove_asset`
prend l'id du lien…) n'est **pas dupliqué ici** : il vit dans
`rapidocms/reference/outils-marque.md`.

## Principes

- **KB → CMS (descendante)** : un changement charte validé dans la KB peut être
  répercuté sur la marque via `gestion-marques`/`edit_brand` (skills du plugin
  `rapidocms`), **après confirmation**, **jamais en silence**.
- **CMS → KB (ascendante)** : une divergence détectée (skill
  `contenu-conforme-marque`) est **signalée**, jamais écrasée automatiquement.
- **Ancre de sync** : la ligne `> Miroir CMS : brand_id <id> — dernière sync
  <YYYY-MM-DD>` en pied de `charte-graphique.md` relie la KB à la marque.
  Posée à l'onboarding (`onboarding-entreprise`), relue par `mise-a-jour-kb`.
- **Dégradé gracieux** : plugin `rapidocms` non installé ou MCP indisponible →
  le signaler et continuer ; la sync se fera plus tard. La KB n'attend jamais
  le CMS.

## Skills concernés (plugin rapidocms)
`gestion-marques` (create/edit brand), `bibliotheque-assets` (logo/assets),
`contenu-conforme-marque` (détection de divergence).
