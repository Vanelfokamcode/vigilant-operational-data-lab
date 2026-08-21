import json
from uuid import uuid4

from vigilant_ops_lab.events import record_order_created
from vigilant_ops_lab.schemas import Order


def test_record_order_created_writes_one_json_event(tmp_path) -> None:
    event_log_path = tmp_path / "order_events.jsonl"
    order = Order(
        customer_id=uuid4(),
        amount_cents=1999,
        currency="EUR",
    )

    event = record_order_created(order, event_log_path)

    saved_event = json.loads(event_log_path.read_text(encoding="utf-8"))

    assert saved_event == event
    assert saved_event["event_type"] == "order_created"
    assert saved_event["order_id"] == str(order.order_id)
    assert saved_event["amount_cents"] == 1999
