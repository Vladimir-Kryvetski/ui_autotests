import pytest
from playwright.sync_api import Page
from classes.classes_form import SubmitApplication, Locators

@pytest.fixture(scope="function", autouse=True)
def setup_tests(page: Page):
    base_url = "https://manao-team.com/"
    page.goto(base_url)
    return base_url

@pytest.fixture(scope="function")
def submit_application(page:Page):
    return SubmitApplication(page, Locators)
