from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from orchard_grade.application import Application
from orchard_grade.contracts.batches import ContractError, DomainRecord
from orchard_grade.inspection.receipts import InspectionReceipt


class PackhouseQueueTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.database = Path(temporary.name) / "lots.sqlite3"
        self.application = Application(self.database)
        self.record = DomainRecord("lot-1", {"origin_code": "north", "line_id": "line-a",
            "camera_batch": "camera-1", "sweetness_brix": 19, "diameter_mm": 72,
            "mass_g": 105, "bruise_area": 1, "camera_coverage": .9,
            "internal_void": 1, "ct_confidence": .9, "ripeness": .8,
            "harvest_age_h": 12})
        self.application.repository.save_record(self.record)

    def receipt(self, receipt_id="inspection-1", grade="processing"):
        return InspectionReceipt(receipt_id, self.record.record_id, "north", "line-a",
                                 "camera-1", grade, "premium", "random", "2026-11-15T10:00:00Z")

    def test_inspection_provenance_is_stored_and_identity_conflicts_fail(self):
        self.assertTrue(self.application.receive_inspection(self.receipt()))
        self.assertFalse(self.application.receive_inspection(self.receipt()))
        with self.assertRaisesRegex(ContractError, "conflicting"):
            self.application.receive_inspection(self.receipt(grade="standard"))
        self.assertEqual(self.application.repository.inspection_rows("lot-1")[0]["sampling_reason"], "random")

    def test_dispatch_observes_release_and_does_not_rewrite_history(self):
        self.application.receive_inspection(self.receipt())
        with self.assertRaisesRegex(ContractError, "released"):
            self.application.dispatch("lot-1")
        released = DomainRecord(self.record.record_id, self.record.payload, "released", 2,
                                self.record.occurred_at, self.record.source)
        self.application.repository.save_record(released, expected_version=1)
        self.assertEqual(self.application.dispatch("lot-1")["destination"], "processing")
        self.assertEqual(self.application.dispatch("lot-1")["destination"], "processing")
        self.application.receive_inspection(self.receipt("inspection-2", "standard"))
        with self.assertRaisesRegex(ContractError, "silently"):
            self.application.dispatch("lot-1")
        self.assertEqual(self.application.repository.queue_rows()[0]["destination"], "processing")

    def test_inspection_origin_must_agree_with_record(self):
        invalid = InspectionReceipt("bad", "lot-1", "south", "line-a", "camera-1",
                                    "premium", "premium", "random", "2026-11-15T10:00:00Z")
        with self.assertRaisesRegex(ContractError, "origin"):
            self.application.receive_inspection(invalid)
