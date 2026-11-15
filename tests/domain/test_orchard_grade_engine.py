from __future__ import annotations

import unittest
from orchard_grade.contracts.batches import DomainRecord
from orchard_grade.sensing.fusion import batch_calibration, derive_context, grade_probability, origin_drift


class Repo:
    def __init__(self, rows): self.rows = rows
    def list_records(self): return self.rows


class FusionTests(unittest.TestCase):
    def record(self, key, origin="gx"):
        return DomainRecord(key, {"sweetness_brix": 18, "diameter_mm": 74, "mass_g": 108, "skin_color": "purple",
            "bruise_area": 1, "internal_void": 0.5, "ripeness": 0.8, "origin_code": origin,
            "harvest_age_h": 18, "camera_coverage": 0.98, "ct_confidence": 0.94, "manual_grade": "premium"})

    def test_probabilities_sum_to_one(self):
        values = grade_probability(self.record("a"))
        self.assertAlmostEqual(sum(values.values()), 1.0)
        self.assertGreater(values["premium"], values["processing"])

    def test_batch_and_origin_drift(self):
        rows = [self.record("a", "north"), self.record("b", "south")]
        self.assertEqual(batch_calibration(rows)["sample_count"], 2.0)
        self.assertEqual(origin_drift(rows)["origin_count"], 2.0)
        self.assertIn("calibration_need_weight", derive_context(rows[0], Repo(rows)))
