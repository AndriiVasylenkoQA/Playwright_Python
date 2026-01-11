BASE_URL = "https://reqres.in/api/users/2"

def test_get_user(api_session):
    response = api_session.get(BASE_URL)

    assert response.status_code == 200
    body = response.json()
    print(body)
    assert "data" in body
    assert body["data"]["id"] == 2
    assert body["data"]["email"].endswith("@reqres.in")