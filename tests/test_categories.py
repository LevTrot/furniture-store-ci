def test_create_category(client):
    response = client.post("/categories/", json={"name": "Chairs"})
    assert response.status_code == 200
    assert response.json()["name"] == "Chairs"


def test_get_categories(client):
    client.post("/categories/", json={"name": "Tables"})
    response = client.get("/categories/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_update_category(client):
    res = client.post("/categories/", json={"name": "Old"})
    category_id = res.json()["id"]

    response = client.put(f"/categories/{category_id}", json={"name": "New"})
    assert response.status_code == 200
    assert response.json()["name"] == "New"


def test_delete_category(client):
    res = client.post("/categories/", json={"name": "Delete"})
    category_id = res.json()["id"]

    response = client.delete(f"/categories/{category_id}")
    assert response.status_code == 200