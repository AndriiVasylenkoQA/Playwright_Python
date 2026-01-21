def test_delete_user(api_session):
    response = api_session.delete(api_session.base_url + "/2")

    assert response.status_code == 204
    assert response.text == ""
