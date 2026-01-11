BASE_URL = "https://reqres.in/api/users/2"

def test_post_create_user(api_session):
    payload = {
        "name": "Andrii",
        "job": "QA Engineer"
    }

    response = api_session.post(BASE_URL, json=payload)

    assert response.status_code == 201
    body = response.json()
    print(body)
    assert body["name"] == "Andrii"
    assert body["job"] == "QA Engineer"
    assert "id" in body