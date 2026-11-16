from __future__ import annotations

import sqlite3
from dataclasses import dataclass

from orchard_grade.contracts.batches import ContractError, DomainRecord, stable_hash, utc_now
from orchard_grade.inspection.receipts import receipts_for_lot
from orchard_grade.sensing.fusion import grade_probability


@dataclass(frozen=True)
class QueueAssignment:
    lot_id: str
    destination: str
    reason: str
    evidence_ids: tuple[str, ...]
    record_version: int


def prepare_queue(connection: sqlite3.Connection) -> None:
    connection.execute("""CREATE TABLE IF NOT EXISTS packhouse_queue(
        lot_id TEXT PRIMARY KEY, destination TEXT NOT NULL, reason TEXT NOT NULL,
        evidence_hash TEXT NOT NULL, record_version INTEGER NOT NULL, assigned_at TEXT NOT NULL
    )""")


def plan_assignment(record: DomainRecord, receipts: list[dict]) -> QueueAssignment:
    if record.state == "recalled":
        return QueueAssignment(record.record_id, "hold", "recalled lot", (), record.version)
    if record.state != "released":
        raise ContractError("packhouse queue accepts released lots only")
    if any(receipt["lot_id"] != record.record_id for receipt in receipts):
        raise ContractError("inspection evidence belongs to another lot")
    if receipts:
        latest = sorted(receipts, key=lambda item: (item["inspected_at"], item["receipt_id"]))[-1]
        return QueueAssignment(record.record_id, latest["inspected_grade"], "latest human inspection",
                               (latest["receipt_id"],), record.version)
    probabilities = grade_probability(record)
    destination = max(probabilities, key=probabilities.__getitem__)
    return QueueAssignment(record.record_id, destination, "machine grade; no human inspection",
                           (), record.version)


def assign_released_lot(connection: sqlite3.Connection, record: DomainRecord) -> QueueAssignment:
    prepare_queue(connection)
    assignment = plan_assignment(record, receipts_for_lot(connection, record.record_id))
    evidence_hash = stable_hash({"record": record.fingerprint, "receipts": assignment.evidence_ids})
    existing = connection.execute("SELECT destination,reason,evidence_hash,record_version FROM packhouse_queue WHERE lot_id=?",
                                  (record.record_id,)).fetchone()
    if existing:
        if tuple(existing) != (assignment.destination, assignment.reason, evidence_hash, record.version):
            raise ContractError("existing dispatch cannot be silently replaced")
        return assignment
    connection.execute("INSERT INTO packhouse_queue VALUES(?,?,?,?,?,?)",
                       (record.record_id, assignment.destination, assignment.reason,
                        evidence_hash, record.version, utc_now()))
    return assignment
