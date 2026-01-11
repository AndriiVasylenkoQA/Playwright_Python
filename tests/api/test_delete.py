BASE_URL = "https://reqres.in/api/users/2"

def test_delete_user(api_session):
    response = api_session.delete(BASE_URL)

    assert response.status_code == 204
    assert response.text == ""
