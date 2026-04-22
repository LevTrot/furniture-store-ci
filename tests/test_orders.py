def test_create_order(client):
    response = client.post("/orders/")
    assert response.status_code == 200


def test_get_orders(client):
    client.post("/orders/")
    response = client.get("/orders/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_delete_order(client):
    order = client.post("/orders/").json()
    response = client.delete(f"/orders/{order['id']}")
    assert response.status_code == 200