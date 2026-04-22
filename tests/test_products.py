def test_create_product(client):
    cat = client.post("/categories/", json={"name": "Sofas"}).json()

    response = client.post(
        "/products/",
        json={
            "name": "Big Sofa",
            "price": 500,
            "category_id": cat["id"],
        },
    )

    assert response.status_code == 200


def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200


def test_update_product(client):
    cat = client.post("/categories/", json={"name": "Beds"}).json()

    product = client.post(
        "/products/",
        json={
            "name": "Bed",
            "price": 200,
            "category_id": cat["id"],
        },
    ).json()

    response = client.put(
        f"/products/{product['id']}",
        json={
            "name": "Bed updated",
            "price": 300,
            "category_id": cat["id"],
        },
    )

    assert response.status_code == 200


def test_delete_product(client):
    cat = client.post("/categories/", json={"name": "Temp"}).json()

    product = client.post(
        "/products/",
        json={
            "name": "Temp",
            "price": 1,
            "category_id": cat["id"],
        },
    ).json()

    response = client.delete(f"/products/{product['id']}")
    assert response.status_code == 200