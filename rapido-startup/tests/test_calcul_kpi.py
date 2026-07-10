#!/usr/bin/env python3
"""Tests unitaires de scripts/calcul_kpi.py (stdlib unittest).

Les exemples chiffrés sont ceux de references/formules-kpi.md.
Lancer : python3 -m unittest rapido-startup/tests/test_calcul_kpi.py -v
(ou python3 rapido-startup/tests/test_calcul_kpi.py)"""
import json
import math
import os
import subprocess
import sys
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "..", "skills", "catalogue-kpi", "scripts", "calcul_kpi.py")
sys.path.insert(0, os.path.dirname(SCRIPT))
import calcul_kpi as k  # noqa: E402


class TestFonctionsPures(unittest.TestCase):
    def test_ltv_exemple_reference(self):
        """ARPU 99 € × marge 80 % ÷ churn 5 % = 1584 € (exemple du catalogue)."""
        self.assertEqual(k.ltv(99, 0.80, 0.05), 1584.0)

    def test_churn_annualise_compose_pas_x12(self):
        """5 %/mois → 45,96 %/an (composé), PAS 60 % (×12)."""
        self.assertEqual(k.churn_annualise_compose(0.05), 0.4596)
        self.assertNotAlmostEqual(k.churn_annualise_compose(0.05), 0.60, places=2)

    def test_mrr_contrat_annuel_divise_par_12(self):
        """Contrat annuel 1200 € = 100 €/mois de MRR, pas 1200 le mois de signature."""
        abonnements = [{"montant": 99, "periodicite": "mensuel"},
                       {"montant": 1200, "periodicite": "annuel"}]
        self.assertEqual(k.mrr(abonnements), 199.0)

    def test_decompose_mrr(self):
        self.assertEqual(k.decompose_mrr(500, 200, 100, 300), 300.0)

    def test_nrr_base_existante(self):
        """10 000 début, +800 expansion, −200 contraction, −600 churn → NRR 100 %."""
        self.assertEqual(k.nrr(10000, 800, 200, 600), 1.0)

    def test_arpu_et_churn(self):
        self.assertEqual(k.arpu(9900, 100), 99.0)
        self.assertEqual(k.churn_rate(200, 10), 0.05)

    def test_unit_economics(self):
        self.assertEqual(k.cac(6000, 12), 500.0)
        self.assertEqual(k.ltv_cac(1584, 500), 3.17)
        self.assertEqual(k.cac_payback(500, 99, 0.80), 6.3)

    def test_rentabilite(self):
        self.assertEqual(k.marge_brute(10000, 2000), 0.8)
        self.assertEqual(k.burn_net(30000, 10000), 20000.0)
        self.assertEqual(k.runway(120000, 20000), 6.0)
        self.assertEqual(k.runway(120000, 0), math.inf)  # rentable
        self.assertEqual(k.rule_of_40(25, 10), 35.0)
        self.assertEqual(k.break_even_mrr(8000, 0.80), 10000.0)

    def test_dso(self):
        """15 000 € de créances sur 45 000 € de CA sur 90 j → DSO 30 j."""
        self.assertEqual(k.dso(15000, 45000, 90), 30.0)

    def test_commercial(self):
        self.assertEqual(k.velocite_pipeline(20, 0.25, 3000, 30), 500.0)
        self.assertEqual(k.pipeline_coverage(90000, 30000), 3.0)

    def test_restauration_et_services(self):
        self.assertEqual(k.food_cost(3100, 10000), 0.31)
        self.assertEqual(k.ticket_moyen(10000, 400), 25.0)
        self.assertEqual(k.charge_vs_contrat(38.5, 35), 1.1)
        self.assertEqual(k.cout_revient_projet(120, 65, 800), 8600.0)


class TestStatuts(unittest.TestCase):
    def test_ltv_cac_seuil_defaut(self):
        r = k.calculer({"kpi": "ltv_cac", "entrees": {"ltv_valeur": 1584, "cac_valeur": 500}})
        self.assertEqual(r["valeur"], 3.17)
        self.assertEqual(r["statut"], "ok")
        self.assertIn("1584", r["formule_appliquee"])

    def test_runway_alerte(self):
        r = k.calculer({"kpi": "runway", "entrees": {"tresorerie": 50000, "burn_net_mensuel": 10000}})
        self.assertEqual(r["valeur"], 5.0)
        self.assertEqual(r["statut"], "alerte")  # < 6 mois

    def test_seuil_kb_prime_sur_defaut(self):
        """Un seuil maison passé en entrée écrase le défaut secteur."""
        r = k.calculer({"kpi": "dso", "entrees": {"creances_clients": 15000,
                                                  "ca_periode": 45000, "jours_periode": 90},
                        "seuil": {"type": "max", "valeur": 25.0},
                        "source_seuil": "rapido-kb/processus-internes.md"})
        self.assertEqual(r["valeur"], 30.0)
        self.assertEqual(r["statut"], "alerte")  # 30 > 25 (seuil maison)
        self.assertEqual(r["seuil"]["source"], "rapido-kb/processus-internes.md")

    def test_food_cost_plage(self):
        r = k.calculer({"kpi": "food_cost", "entrees": {"cout_matieres": 3100, "ca_nourriture": 10000}})
        self.assertEqual(r["statut"], "ok")  # 31 % dans 28-35 %


class TestMainCLI(unittest.TestCase):
    def test_cli_json(self):
        demande = json.dumps({"kpi": "ltv", "entrees": {"arpu_mensuel": 99,
                              "marge_brute_ratio": 0.80, "churn_mensuel": 0.05}})
        r = subprocess.run(["python3", SCRIPT], input=demande,
                           capture_output=True, text=True)
        sortie = json.loads(r.stdout)
        self.assertEqual(r.returncode, 0)
        self.assertEqual(sortie["valeur"], 1584.0)
        self.assertIn("99", sortie["formule_appliquee"])

    def test_cli_kpi_inconnu(self):
        r = subprocess.run(["python3", SCRIPT], input='{"kpi": "roi_magique", "entrees": {}}',
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("KPI inconnu", json.loads(r.stdout)["erreur"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
