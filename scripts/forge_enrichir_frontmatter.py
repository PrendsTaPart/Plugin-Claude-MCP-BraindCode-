#!/usr/bin/env python3
"""Enrichit le frontmatter des 180 skills rapido-forge avec `tags` (1-3,
taxonomie FERMÉE à 12) et `niveau` (debutant|intermediaire|expert), déduits
du nom et du contenu. Idempotent : remplace tags/niveau existants sans
doublonner ; name/description jamais modifiés.

Usage : python3 forge_enrichir_frontmatter.py [--apply]   (défaut : dry-run)
"""
import os
import re
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKILLS = os.path.join(RACINE, "rapido-forge", "skills")

TAXONOMIE = ["strategie", "marketing", "vente", "produit", "finance",
             "juridique", "marque", "contenu", "acquisition", "data",
             "organisation", "pitch"]

# mots-clés (sur le NOM) -> tags, appliqués dans l'ordre, max 3 tags
REGLES = [
    (r"pitch|investor|demo-script", ["pitch"]),
    (r"press-release|pr-media", ["pitch", "contenu"]),
    (r"fundraising|cap-table", ["finance", "pitch"]),
    (r"financial|cash-flow|burn|unit-economics|break-even|budget|revenue-model|funding|cost-waterfall", ["finance"]),
    (r"pricing", ["finance", "strategie"]),
    (r"legal|ip-protection", ["juridique"]),
    (r"google-ads|linkedin-ads|meta-ads|tiktok-ads|first-ad|paid|retargeting|pixel", ["acquisition"]),
    (r"cold-email|hunter-outreach", ["acquisition", "vente"]),
    (r"seo|semrush|search-console|lead-magnet|referral|product-hunt|ph-page|pre-launch|influencer|growth-experiments", ["acquisition"]),
    (r"sales|spin|soncas|bant|objections|negotiation|commercial-proposal|upsell", ["vente"]),
    (r"customer-success", ["vente", "organisation"]),
    (r"brand|naming|tagline|tone-of-voice|visual-identity|logo|color-palette", ["marque"]),
    (r"content|editorial|blog|linkedin-posts|social-media|social-strategy|video|voiceover|avatar|course-outline|quiz|about-page|landing-copy|testimonial|launch-post|hero-image", ["contenu"]),
    (r"email-sequence|email-marketing|email-setup", ["marketing", "contenu"]),
    (r"analytics|kpi|dashboard|north-star|ab-testing|heatmaps|google-trends|quantitative|feedback-analysis|nps", ["data"]),
    (r"persona|mvp|wireframe|roadmap|specs|prototype|user-story|user-tests|qa-checklist|feature-benchmark|jtbd|design-system|ui-guidelines|sitemap|changelog|iteration-planning|gamification|customer-journey", ["produit"]),
    (r"funnel|aarrr|conversion|marketing-4|community|launch-plan|launch-checklist|launch-budget", ["marketing"]),
    (r"okr|eisenhower|advisory-board|lessons-learned|stakeholder|certification|rice", ["organisation"]),
    (r"bmc|business-model|lean-canvas|swot|pestel|porter|positioning|market-sizing|market-segmentation|trend|competitive|blue-ocean|ansoff|bcg|golden-circle|vision-mission|scenarios|adoption-curve|growth-strategy|impact-effort|uvp|usp|value-proposition|problem-validation|pain-mapping|qualitative", ["strategie"]),
    (r"automation-workflow|webhook|export-pdf|contact-form", ["organisation", "data"]),
    (r"landing-page|pricing-page", ["produit", "marketing"]),
    (r"lovable-prompt", ["produit"]),
]

RX_NIV_INTER_IDEATION = re.compile(
    r"ads|paid|retargeting|pixel|financial|investor|pitch|pricing|referral|"
    r"email-sequence|cash-flow|automation|webhook|analytics|kpi|growth-experiments")
RX_NIV_EXPERT_SCALE = re.compile(
    r"fundraising|cap-table|unit-economics|burn|break-even|negotiation|"
    r"ab-testing|financial-projections|pricing-strategy|cost-waterfall|scenarios")

# ------------------------------------------------------------- prérequis
# Dépendances pédagogiques (règles du brief v1.1 + chaînage J1→J2 du
# bootcamp d'après reference/parcours.md + analyse de contenu). Toute cible
# doit exister ; le graphe est validé sans cycle par scripts/forge_catalogue.py.
PREREQUIS = {
    # pitch/investor/fundraising <= validation du problème + un skill financier
    "bootcamp-pitch-deck-b5": ["bootcamp-problem-validation", "bootcamp-financial-projections"],
    "bootcamp-pitch-script-b5": ["bootcamp-problem-validation", "bootcamp-financial-projections"],
    "bootcamp-investor-faq": ["bootcamp-problem-validation", "bootcamp-financial-projections"],
    "ideation-pitch-deck": ["bootcamp-problem-validation", "ideation-financial-forecast"],
    "ideation-pitch-script": ["bootcamp-problem-validation", "ideation-financial-forecast"],
    "ideation-investor-faq": ["bootcamp-problem-validation", "ideation-financial-forecast"],
    # ads/pixel/retargeting/paid <= landing + persona
    "ideation-first-ad-campaign": ["ideation-landing-page", "ideation-persona-maker"],
    "ideation-paid-acquisition": ["ideation-landing-page", "ideation-persona-maker"],
    "ideation-retargeting-setup": ["ideation-landing-page", "ideation-persona-maker"],
    "scale-google-ads-setup": ["ideation-landing-page", "ideation-persona-maker"],
    "scale-linkedin-ads-b2b": ["ideation-landing-page", "ideation-persona-maker"],
    "scale-linkedin-pixel": ["ideation-landing-page", "ideation-persona-maker"],
    "scale-meta-ads-campaign": ["ideation-landing-page", "ideation-persona-maker"],
    "scale-meta-pixel": ["ideation-landing-page", "ideation-persona-maker"],
    "scale-tiktok-ads-creator": ["ideation-landing-page", "ideation-persona-maker"],
    "scale-tiktok-pixel": ["ideation-landing-page", "ideation-persona-maker"],
    # finance scale <= prévisionnel d'idéation
    "scale-unit-economics": ["ideation-financial-forecast"],
    "scale-burn-rate": ["ideation-financial-forecast"],
    "scale-break-even": ["ideation-financial-forecast"],
    # règles nommées du brief
    "bootcamp-bmc-complete": ["bootcamp-persona-deep", "bootcamp-problem-validation"],
    "ideation-launch-plan": ["ideation-landing-page", "ideation-launch-checklist"],
    "scale-fundraising-plan": ["scale-unit-economics", "scale-financial-projections"],
    # chaînage J1 -> J2 du bootcamp (reference/parcours.md)
    "bootcamp-problem-validation": ["bootcamp-qualitative-study"],
    "bootcamp-pain-mapping": ["bootcamp-qualitative-study"],
    "bootcamp-persona-deep": ["bootcamp-market-segmentation"],
    "bootcamp-pestel-analysis": ["bootcamp-trend-analysis"],
    "bootcamp-porter-forces": ["bootcamp-market-sizing-b5"],
    "bootcamp-competitive-deep": ["bootcamp-market-segmentation"],
    "bootcamp-feature-benchmark": ["bootcamp-competitive-deep"],
    "bootcamp-positioning-map": ["bootcamp-competitive-deep"],
    "bootcamp-competitive-advantage": ["bootcamp-positioning-map"],
    # analyse de contenu (compléments)
    "scale-financial-projections": ["ideation-financial-forecast"],
    "scale-pricing-strategy": ["scale-unit-economics"],
    "ideation-pricing-page": ["ideation-value-proposition"],
    "ideation-landing-page": ["ideation-value-proposition", "ideation-persona-maker"],
}

RX_FRONT = re.compile(r"\A(---\s*\n)(.*?)(\n---\s*\n)", re.S)


def deduire(nom, contenu):
    tags = []
    for motif, ts in REGLES:
        if re.search(motif, nom):
            for t in ts:
                if t not in tags:
                    tags.append(t)
        if len(tags) >= 3:
            break
    if not tags:  # repli : chercher dans le contenu (titres/objectif)
        tete = contenu[:600].lower()
        for motif, ts in REGLES:
            if re.search(motif, tete):
                tags = [t for t in ts][:2]
                break
    if not tags:
        tags = ["strategie"]
    tags = tags[:3]
    assert all(t in TAXONOMIE for t in tags), (nom, tags)

    if nom.startswith("bootcamp-"):
        niveau = "debutant"
    elif nom.startswith("ideation-"):
        niveau = "intermediaire" if RX_NIV_INTER_IDEATION.search(nom) else "debutant"
    else:
        niveau = "expert" if RX_NIV_EXPERT_SCALE.search(nom) else "intermediaire"
    return tags, niveau


def main():
    apply_ = "--apply" in sys.argv
    lignes = []
    for d in sorted(os.listdir(SKILLS)):
        f = os.path.join(SKILLS, d, "SKILL.md")
        if not os.path.isfile(f):
            continue
        src = open(f, encoding="utf-8").read()
        m = RX_FRONT.match(src)
        assert m, f
        bloc = m.group(2)
        tags, niveau = deduire(d, src[m.end():])
        # idempotence : retirer tags/niveau existants
        bloc_nettoye = re.sub(r"^(tags|niveau|prerequis):.*(?:\n(?:  - .*|- .*))*\n?", "", bloc, flags=re.M).rstrip("\n")
        nouveau_bloc = (bloc_nettoye + "\ntags: [" + ", ".join(tags) + "]"
                        + "\nniveau: " + niveau)
        if d in PREREQUIS:
            nouveau_bloc += "\nprerequis: [" + ", ".join(PREREQUIS[d]) + "]" 
        if apply_:
            open(f, "w", encoding="utf-8").write(
                m.group(1) + nouveau_bloc + m.group(3) + src[m.end():])
        lignes.append((d, ", ".join(tags), niveau))
    largeur = max(len(l[0]) for l in lignes)
    for nom, tags, niveau in lignes:
        print(f"{nom.ljust(largeur)} | {tags.ljust(34)} | {niveau}")
    print(f"\n{'APPLIQUÉ' if apply_ else 'DRY-RUN'} — {len(lignes)} skills")


if __name__ == "__main__":
    main()
