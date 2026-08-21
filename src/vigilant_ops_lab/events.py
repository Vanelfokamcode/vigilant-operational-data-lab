"""Write local operational events as newline-delimited JSON."""

import json
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from vigilant_ops_lab.schemas import Order

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EVENT_LOG_PATH = PROJECT_ROOT / "data" / "raw" / "order_events.jsonl"


def record_order_created(
    order: Order,
    event_log_path: Path = DEFAULT_EVENT_LOG_PATH,
) -> dict[str, str | int]:
    """Record one order_created event in the local event journal."""
    event_log_path.parent.mkdir(parents=True, exist_ok=True)

    event = {
        "event_id": str(uuid4()),
        "event_type": "order_created",
        "event_version": 1,
        "event_at": datetime.now(UTC).isoformat(),
        "source": "order_api",
        "order_id": str(order.order_id),
        "customer_id": str(order.customer_id),
        "amount_cents": order.amount_cents,
        "currency": order.currency,
        "order_status": order.status,
    }

    with event_log_path.open("a", encoding="utf-8") as event_file:
        event_file.write(json.dumps(event) + "\n")

    return event
