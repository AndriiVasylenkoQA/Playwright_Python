def test_get_user(api_session):
    response = api_session.get(api_session.base_url + "/2")

    assert response.status_code == 200
    body = response.json()
    print(body)
    assert "data" in body
    assert body["data"]["id"] == 2
    assert body["data"]["email"].endswith("@reqres.in")