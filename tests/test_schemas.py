from datetime import UTC
from uuid import uuid4

import pytest
from pydantic import ValidationError

from vigilant_ops_lab.schemas import Order, OrderCreate, OrderStatus


def test_order_create_accepts_a_valid_order() -> None:
    order = OrderCreate(
        customer_id=uuid4(),
        amount_cents=1999,
    )

    assert order.amount_cents == 1999
    assert order.currency == "EUR"


def test_order_create_rejects_a_zero_amount() -> None:
    with pytest.raises(ValidationError):
        OrderCreate(
            customer_id=uuid4(),
            amount_cents=0,
        )


def test_order_create_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        OrderCreate(
            customer_id=uuid4(),
            amount_cents=1999,
            discount_code="NOT_SUPPORTED_YET",
        )


def test_order_record_starts_pending() -> None:
    order = Order(
        customer_id=uuid4(),
        amount_cents=1999,
        currency="EUR",
    )

    assert order.status is OrderStatus.PENDING
    assert order.created_at.tzinfo is UTC
