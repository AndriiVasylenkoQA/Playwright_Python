import os
import pytest
import requests
from playwright.sync_api import sync_playwright

BASE_URL = "https://reqres.in/api/users"

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=True)
       yield browser
       browser.close()

@pytest.fixture
def page(browser):
   page = browser.new_page()
   yield page
   page.close()

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.base_url = BASE_URL
    api_key = os.getenv("REQRES_API_KEY", "DUMMY_KEY")
    session.headers.update({
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    })
    yield session
    session.close()