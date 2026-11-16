from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from typing import Any

from orchard_grade.contracts.batches import ContractError, canonical_json, stable_hash, utc_now


@dataclass(frozen=True)
class InspectionReceipt:
    receipt_id: str
    lot_id: str
    origin_code: str
    line_id: str
    camera_batch: str
    inspected_grade: str
    machine_grade: str
    sampling_reason: str
    inspected_at: str

    def __post_init__(self) -> None:
        if not all((self.receipt_id, self.lot_id, self.origin_code, self.line_id,
                    self.camera_batch, self.inspected_grade, self.machine_grade,
                    self.sampling_reason, self.inspected_at)):
            raise ContractError("inspection receipt requires evidence identity and sampling provenance")
        if self.inspected_grade not in {"premium", "standard", "processing"}:
            raise ContractError("unknown inspected grade")
        if self.machine_grade not in {"premium", "standard", "processing"}:
            raise ContractError("unknown machine grade")

    @property
    def fingerprint(self) -> str:
        return stable_hash(self.__dict__)


def prepare_receipts(connection: sqlite3.Connection) -> None:
    connection.execute("""CREATE TABLE IF NOT EXISTS inspection_receipts(
        receipt_id TEXT PRIMARY KEY, lot_id TEXT NOT NULL, origin_code TEXT NOT NULL,
        line_id TEXT NOT NULL, camera_batch TEXT NOT NULL, inspected_grade TEXT NOT NULL,
        machine_grade TEXT NOT NULL, sampling_reason TEXT NOT NULL,
        inspected_at TEXT NOT NULL, receipt_json TEXT NOT NULL, fingerprint TEXT NOT NULL,
        recorded_at TEXT NOT NULL
    )""")
    connection.execute("CREATE INDEX IF NOT EXISTS idx_receipts_lot ON inspection_receipts(lot_id, inspected_at)")


def record_receipt(connection: sqlite3.Connection, receipt: InspectionReceipt) -> bool:
    prepare_receipts(connection)
    row = connection.execute("SELECT fingerprint FROM inspection_receipts WHERE receipt_id=?",
                             (receipt.receipt_id,)).fetchone()
    if row:
        if row[0] != receipt.fingerprint:
            raise ContractError("conflicting inspection receipt identity")
        return False
    connection.execute("""INSERT INTO inspection_receipts VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (receipt.receipt_id, receipt.lot_id, receipt.origin_code, receipt.line_id,
                        receipt.camera_batch, receipt.inspected_grade, receipt.machine_grade,
                        receipt.sampling_reason, receipt.inspected_at, canonical_json(receipt.__dict__),
                        receipt.fingerprint, utc_now()))
    return True


def receipts_for_lot(connection: sqlite3.Connection, lot_id: str) -> list[dict[str, Any]]:
    prepare_receipts(connection)
    rows = connection.execute("SELECT receipt_json FROM inspection_receipts WHERE lot_id=? ORDER BY inspected_at,receipt_id",
                              (lot_id,)).fetchall()
    return [json.loads(row[0]) for row in rows]
