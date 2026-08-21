from fastapi.testclient import TestClient

from vigilant_ops_lab.main import app

client = TestClient(app)

CUSTOMER_ID = "550e8400-e29b-41d4-a716-446655440000"


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_order_returns_a_new_pending_order() -> None:
    response = client.post(
        "/orders",
        json={
            "customer_id": CUSTOMER_ID,
            "amount_cents": 1999,
            "currency": "EUR",
        },
    )

    body = response.json()

    assert response.status_code == 201
    assert body["customer_id"] == CUSTOMER_ID
    assert body["amount_cents"] == 1999
    assert body["currency"] == "EUR"
    assert body["status"] == "pending"
    assert "order_id" in body
    assert "created_at" in body


def test_create_order_rejects_a_zero_amount() -> None:
    response = client.post(
        "/orders",
        json={
            "customer_id": CUSTOMER_ID,
            "amount_cents": 0,
        },
    )

    assert response.status_code == 422


def test_create_order_rejects_an_unknown_field() -> None:
    response = client.post(
        "/orders",
        json={
            "customer_id": CUSTOMER_ID,
            "amount_cents": 1999,
            "discount_code": "NOT_SUPPORTED_YET",
        },
    )

    assert response.status_code == 422
