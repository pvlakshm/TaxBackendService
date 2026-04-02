import pytest
from fastapi.testclient import TestClient
from main import app

# --- Fixtures ---

@pytest.fixture
def client():
    """Provides a clean FastAPI test client."""
    return TestClient(app)

@pytest.fixture
def base_payload():
    """A helper to generate standard input data."""
    return {
        "refund_amount": 50.0,
        "total_amount": 100.0,
        "tax_paid": 15.0
    }

# --- Tests (Arrange, Act, Assert) ---

def test_calculate_standard_50_percent_refund(client, base_payload):
    # Arrange
    # (50/100) * 15 = 7.50
    expected_refund = 7.50

    # Act
    response = client.post("/api/v1/calculate", json=base_payload)
    
    # Assert
    assert response.status_code == 200
    assert response.json()["tax_refund"] == expected_refund
    assert response.json()["formula_version"] == "1.0"

def test_calculate_100_percent_full_refund(client, base_payload):
    # Arrange
    # Updating the fixture data for a full refund
    base_payload["refund_amount"] = 100.0
    expected_refund = 15.00

    # Act
    response = client.post("/api/v1/calculate", json=base_payload)
    
    # Assert
    assert response.status_code == 200
    assert response.json()["tax_refund"] == expected_refund

def test_calculate_precision_rounding_up(client, base_payload):
    # Arrange
    # (10/100) * 15.55 = 1.555 -> Should round to 1.56
    base_payload.update({"refund_amount": 10.0, "tax_paid": 15.55})
    expected_refund = 1.56

    # Act
    response = client.post("/api/v1/calculate", json=base_payload)
    
    # Assert
    assert response.json()["tax_refund"] == expected_refund

def test_calculate_precision_rounding_down(client, base_payload):
    # Arrange
    # (10/100) * 15.54 = 1.554 -> Should round to 1.55
    base_payload.update({"refund_amount": 10.0, "tax_paid": 15.54})
    expected_refund = 1.55

    # Act
    response = client.post("/api/v1/calculate", json=base_payload)
    
    # Assert
    assert response.json()["tax_refund"] == expected_refund

def test_zero_tax_paid_results_in_zero_refund(client, base_payload):
    # Arrange
    base_payload["tax_paid"] = 0.0
    expected_refund = 0.0

    # Act
    response = client.post("/api/v1/calculate", json=base_payload)
    
    # Assert
    assert response.json()["tax_refund"] == expected_refund

def test_zero_refund_amount_results_in_zero_refund(client, base_payload):
    # Arrange
    base_payload["refund_amount"] = 0.0
    expected_refund = 0.0

    # Act
    response = client.post("/api/v1/calculate", json=base_payload)
    
    # Assert
    assert response.json()["tax_refund"] == expected_refund

def test_invalid_data_type_returns_422(client, base_payload):
    # Arrange
    base_payload["refund_amount"] = "not-a-number"

    # Act
    response = client.post("/api/v1/calculate", json=base_payload)

    # Assert
    # Proves our API Contract enforces strict types via Pydantic
    assert response.status_code == 422