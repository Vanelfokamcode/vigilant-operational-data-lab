"""HTTP entry point for Vigilant Operational Data Lab."""

from fastapi import FastAPI, status

from vigilant_ops_lab.events import record_order_created
from vigilant_ops_lab.schemas import Order, OrderCreate

app = FastAPI(
    title="Vigilant Operational Data Lab",
    description="A local learning API for operational data and reliability.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Confirm that the API process is reachable."""
    return {"status": "ok"}


@app.post(
    "/orders",
    response_model=Order,
    status_code=status.HTTP_201_CREATED,
    tags=["orders"],
)
def create_order(order_request: OrderCreate) -> Order:
    """Validate an order, then record its creation as an operational event."""
    new_order = Order(**order_request.model_dump())

    record_order_created(new_order)

    return new_order
