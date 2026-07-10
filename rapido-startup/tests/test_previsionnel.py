#!/usr/bin/env python3
"""Tests de scripts/previsionnel.py et du hook garde-projection-realiste.

Lancer : python3 rapido-startup/tests/test_previsionnel.py"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "..", "skills", "plan-financier-previsionnel", "scripts", "previsionnel.py")
HOOK = os.path.join(ICI, "..", "hooks", "scripts", "garde-projection-realiste.py")
sys.path.insert(0, os.path.dirname(SCRIPT))
import previsionnel as p  # noqa: E402

HYPOTHESES = {
    "tresorerie_initiale": 50000, "clients_initiaux": 0,
    "nouveaux_clients_mois": 5, "croissance_mensuelle": 0.10,
    "churn_mensuel": 0.03, "arpu": 99, "cogs_pct": 0.15, "cac": 400,
    "salaires_bruts_mensuels": 8000, "coeff_charges": 1.45,
    "embauches": [{"mois": 7, "brut": 3000}], "couts_fixes_mensuels": 2500,
}


class TestModele(unittest.TestCase):
    def test_36_mois_et_colonnes(self):
        lignes = p.simuler(HYPOTHESES)
        self.assertEqual(len(lignes), 36)
        self.assertEqual(list(lignes[0].keys()), p.COLONNES)

    def test_churn_compose_mois_par_mois(self):
        """Mois 2 : clients = m1 × (1 − churn) + nouveaux, pas m1 + nouveaux − churn×m0."""
        lignes = p.simuler(dict(HYPOTHESES, nouveaux_clients_mois=10,
                                croissance_mensuelle=0.0, churn_mensuel=0.10))
        self.assertEqual(lignes[0]["clients"], 10.0)
        self.assertEqual(lignes[1]["clients"], 19.0)  # 10×0.9 + 10

    def test_salaires_charges_1_45_et_embauche_mois_7(self):
        lignes = p.simuler(HYPOTHESES)
        self.assertEqual(lignes[0]["salaires_charges"], round(8000 * 1.45, 2))
        self.assertEqual(lignes[6]["salaires_charges"], round(11000 * 1.45, 2))  # mois 7

    def test_point_mort_et_besoin_financement(self):
        lignes = p.simuler(HYPOTHESES)
        syn = p.synthese(lignes)
        self.assertIsNotNone(syn["point_mort_mois"])  # croise sur 36 mois avec ces hypothèses
        self.assertGreaterEqual(syn["besoin_financement"], 0)
        # le besoin de financement est bien le creux max : trésorerie min = -besoin (si négatif)
        creux = min(l["tresorerie"] for l in lignes)
        if creux < 0:
            self.assertEqual(syn["besoin_financement"], round(-creux, 2))

    def test_scenarios_ordonnes(self):
        """Upside > base > downside sur le MRR mois 36."""
        res = {nom: p.synthese(p.simuler(h)) for nom, h in p.scenarios(HYPOTHESES).items()}
        self.assertGreater(res["upside"]["mrr_mois_36"], res["base"]["mrr_mois_36"])
        self.assertGreater(res["base"]["mrr_mois_36"], res["downside"]["mrr_mois_36"])

    def test_sensibilite_4x4(self):
        matrice = p.sensibilite(HYPOTHESES)
        self.assertEqual(len(matrice), 4)
        self.assertEqual(len(matrice[0]), 5)  # churn + 4 colonnes CAC

    def test_rejet_churn_zero(self):
        with self.assertRaises(ValueError):
            p.valider(dict(HYPOTHESES, churn_mensuel=0))

    def test_rejet_croissance_35_pct_sans_justification(self):
        with self.assertRaises(ValueError):
            p.valider(dict(HYPOTHESES, croissance_mensuelle=0.35))
        # avec justification : passe
        p.valider(dict(HYPOTHESES, croissance_mensuelle=0.35,
                       justification_croissance="contrat cadre signé le 2026-06 (hypotheses.md)"))


class TestCLIEtFichiers(unittest.TestCase):
    def test_cli_ecrit_les_fichiers(self):
        with tempfile.TemporaryDirectory() as tmp:
            demande = json.dumps(dict(HYPOTHESES, dossier_sortie=tmp))
            r = subprocess.run(["python3", SCRIPT], input=demande,
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            for f in ["previsionnel-base.csv", "previsionnel-upside.csv",
                      "previsionnel-downside.csv", "sensibilite.csv", "PREVISIONNEL.md"]:
                self.assertTrue(os.path.isfile(os.path.join(tmp, f)), f)
            sortie = json.loads(r.stdout)
            self.assertIn("scenarios", sortie)
            md = open(os.path.join(tmp, "PREVISIONNEL.md")).read()
            self.assertIn("scénarios ≠ promesses", md.lower())

    def test_cli_rejette_churn_zero(self):
        demande = json.dumps(dict(HYPOTHESES, churn_mensuel=0, dossier_sortie="/tmp/ignore"))
        r = subprocess.run(["python3", SCRIPT], input=demande, capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertIn("churn", json.loads(r.stdout)["erreur"])


class TestHook(unittest.TestCase):
    def _hook(self, tool_input):
        return subprocess.run(["python3", HOOK],
                              input=json.dumps({"tool_name": "Write", "tool_input": tool_input}),
                              capture_output=True, text=True).returncode

    def test_deny_churn_zero(self):
        self.assertEqual(self._hook({"file_path": "rapido-kb/startup/business-plan/previsionnel/x.json",
                                     "content": '{"churn_mensuel": 0, "arpu": 99}'}), 2)

    def test_deny_croissance_sans_justification(self):
        self.assertEqual(self._hook({"file_path": "notes-previsionnel.md",
                                     "content": '"croissance_mensuelle": 0.40'}), 2)

    def test_allow_croissance_justifiee(self):
        self.assertEqual(self._hook({"file_path": "x-previsionnel.json",
                                     "content": '{"croissance_mensuelle": 0.40, "justification_croissance": "contrat cadre signé (hypotheses.md)"}'}), 0)

    def test_allow_hors_perimetre(self):
        self.assertEqual(self._hook({"file_path": "README.md", "content": "churn_mensuel: 0"}), 0)


if __name__ == "__main__":
    unittest.main(verbosity=1)
