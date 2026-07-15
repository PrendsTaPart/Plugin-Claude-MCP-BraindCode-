# Registre des tunnels de vente

> Modèle. Copié dans `./rapido-kb/marketing/tunnels.md`. Registre à **IDs réels**
> tenu par le skill `tunnel-de-vente-360` — chaque tunnel construit y est tracé.
> Datez chaque entrée.

## Tunnel : (nom du produit)
- **Schéma** : étapes (TOFU→MOFU→BOFU), messages par étape, KPI cibles.
- **IDs des briques** (renseignés à la construction) :
  | Brique | Outil | ID réel |
  |---|---|---|
  | Campagne CMS | `create_campagne` | (id) |
  | Landing / template | `create_editor_template` | (id + URL) |
  | Segment | `create_segment` | (id) |
  | Séquence email | `create_template_email` | (id) |
  | Workflow n8n | n8n | (workflowId) |
  | Projet RH | `create-project-tool` | (id) |
- **Statut** : (acte en cours) / activé le (date).
