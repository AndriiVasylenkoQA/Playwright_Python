def test_put_update_user(api_session):
    payload = {
        "name": "Andrii Updated",
        "job": "General QA"
    }

    response = api_session.put(api_session.base_url + "/2", json=payload)

    assert response.status_code == 200
    body = response.json()
    print(body)

    assert body["name"] == "Andrii Updated"
    assert body["job"] == "General QA"
    assert "updatedAt" in body