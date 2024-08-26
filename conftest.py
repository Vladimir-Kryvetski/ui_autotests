import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function", autouse=True)
def setup_tests(page: Page):
    base_url = "https://manao-team.com/"
    page.goto(base_url)
    return base_url