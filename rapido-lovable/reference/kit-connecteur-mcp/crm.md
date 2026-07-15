# Fiche kit — RapidoCRM

**Kit v1 · 2026-07-15.** Voir `_commun.md` pour le template, la sécurité et les critères.

## Variables d'environnement (immuables)

| Rôle | Nom |
|---|---|
| URL MCP | `RAPIDOCRM_MCP_URL` (valeur produit : `https://crm.rapidosoftware.com/mcp`) |
| Token tenant (quand dispo, §7) | `RAPIDOCRM_MCP_TOKEN` |
| Scope société | `RAPIDOCRM_COMPANY_ID` |
| Clé Anthropic client | `ANTHROPIC_API_KEY` |

Nom du serveur : `rapidocrm`. Edge function : `agent-crm`.

## Familles d'outils autorisées (agent de site / capture)

- **Lecture** : pipeline, produits, RDV du jour, stats de tableau de bord (ex. `get_pipeline`,
  `list_products`, `get_today_schedule`).
- **Écriture — proposée puis confirmée** : capturer un lead (`create_contact`,
  `enregistrer_prospect`), placer en pipeline (`ajouter_prospect_pipeline`), poser un RDV
  (`create_rdv`). **Jamais** sans `approved:true`.
- **Interdit par défaut** : envois (email/SMS/newsletter), factures, suppressions — un
  agent public ne déclenche pas d'envoi ni d'écriture financière (garde-fou symétrique aux
  hooks `garde-envois`/`garde-destructif`).

## Bloc system prompt

```
Tu es l'assistant commercial du site. Tu opères STRICTEMENT dans la société
{RAPIDOCRM_COMPANY_ID}. Langue : français.
Tu peux CONSULTER : offre, pipeline, disponibilités de RDV.
Tu peux CAPTURER un prospect ou proposer un RDV — action PROPOSÉE puis CONFIRMÉE dans
l'UI avant exécution. Tu n'envoies jamais d'email/SMS et ne touches jamais aux factures.
Rien d'inventé ; consentement RGPD requis avant toute capture de contact.
```

## Cas d'usage typiques

« Je veux un devis » → l'agent qualifie, propose la capture du contact (confirmation) +
un RDV · « Quels produits proposez-vous ? » (lecture).
