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

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Test Case Description</th>")
    cells.insert(2, "<th>Form Name</th>")
    cells.insert(3, "<th>Form Page</th>")
    cells.pop(-1)
    cells.pop(-1)
    cells.pop(-1)


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(1, f"<td>{getattr(report, 'test_case', 'N/A')}</td>")
    cells.insert(2, f"<td>{getattr(report, 'form_name', 'N/A')}</td>")
    cells.insert(3, f"<td>{getattr(report, 'form_page', 'N/A')}</td>")
    cells.pop(-1)
    cells.pop(-1)
    cells.pop(-1)
    

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.test_case = getattr(item, 'test_case', item.name)
    report.form_page = getattr(item, 'form_page', '')
    report.form_name = getattr(item, 'form_name', '')
    
    
