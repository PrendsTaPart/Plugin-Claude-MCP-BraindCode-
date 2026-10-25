---
name: publier-la-vitrine
description: Utiliser quand la vitrine Build d'un projet se publie — « publie la vitrine », « qu'est-ce qui manque au readiness ? », « mets la démo en ligne ». Readiness d'abord, chaque manque comblé par une source réelle, deploy après validation humaine, publication sur accord.
---

# Publier la vitrine

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` (vitrines
  incomplètes, business model jamais inventé).

## Démarche
1. **Readiness** : `check_project_readiness` — la liste exacte des
   manques. Puis chaque élément se comble par une SOURCE RÉELLE :
   - **demo_url** : `deploy_project` — SEULEMENT après la validation
     humaine de kind mise_en_ligne (request_human_validation →
     get_pending_validations ; le hook garde-mise-en-ligne refuse sinon) ;
   - **tutoriel** : rédigé depuis le code lu (`read_file`) et le parcours
     TESTÉ — pas depuis l'intention ;
   - **how_it_works** : données, outils MCP, sécurité (ce que l'app fait
     vraiment) ;
   - **business_model / pricing_offer** : UNIQUEMENT sur indication de
     l'humain — jamais inventés, champ vide et dit sinon ;
   - **cover_image_url** : l'image officielle de l'idée ou un visuel
     validé ;
   - **figma_urls, video_url, mcp_server_url, repo_url, marketplace_url** :
     les liens réels enregistrés au fil du chantier.
2. **Publier** : `publish_project` SUR ACCORD EXPLICITE (hook
   garde-build) ; `unpublish_project` reste disponible.
3. **Promotion** : déléguée à rapidocms (brouillon de posts) ou
   rapido-prospector (calendrier éditorial) s'ils sont installés — rien ne
   part d'ici.

## Pièges
- Une vitrine « lauréat » sans tutoriel reste incomplète : le statut ne
  dispense pas du contenu (relevé du 2026-10-25 : les 20 publiées).
- Un deploy « pour la capture » est une mise en ligne PUBLIQUE : même
  validation.

## Dégradation propre
Un élément incomplétable aujourd'hui (vidéo absente, business model non
décidé) : publier se REPORTE ou se fait en l'assumant à l'écran — jamais
de remplissage.
