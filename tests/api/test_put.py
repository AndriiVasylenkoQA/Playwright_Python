BASE_URL = "https://reqres.in/api/users/2"

def test_put_update_user(api_session):
    payload = {
        "name": "Andrii Updated",
        "job": "General QA"
    }

    response = api_session.put(BASE_URL, json=payload)

    assert response.status_code == 200
    body = response.json()
    print(body)

    assert body["name"] == "Andrii Updated"
    assert body["job"] == "General QA"
    assert "updatedAt" in body