
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_get_meals():
    response = client.get("/meals")

    assert response.status_code == 200
    assert "meals" in response.json()
    assert "total" in response.json()


def test_recommend_meals():
    response = client.post(
        "/recommend",
        json={"ingredients": ["chicken", "rice"]}
    )

    assert response.status_code == 200

    data = response.json()
    assert "recommendations" in data
    assert len(data["recommendations"]) > 0
