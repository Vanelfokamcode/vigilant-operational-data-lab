"""Data contracts for the order-processing domain."""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class OrderStatus(StrEnum):
    """States an order can have during its lifecycle."""

    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"


class OrderCreate(BaseModel):
    """The data a client must provide to request a new order."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    customer_id: UUID = Field(
        description="Stable identifier of the customer placing the order."
    )
    amount_cents: int = Field(
        gt=0,
        le=10_000_000,
        description="Amount in euro cents. Example: 1999 means €19.99.",
    )
    currency: Literal["EUR"] = Field(
        default="EUR",
        description="Currency accepted by this first version of the service.",
    )


class Order(BaseModel):
    """The order record returned by the system after creation."""

    model_config = ConfigDict(extra="forbid")

    order_id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    amount_cents: int
    currency: Literal["EUR"]
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
