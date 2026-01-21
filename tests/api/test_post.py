def test_post_create_user(api_session):
    payload = {
        "name": "Andrii",
        "job": "QA Engineer"
    }

    response = api_session.post(api_session.base_url, json=payload)

    assert response.status_code == 201
    body = response.json()
    print(body)
    assert body["name"] == "Andrii"
    assert body["job"] == "QA Engineer"
    assert "id" in body