import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def setup_report(request):
    request.node.error_message = ''
    def _add_error_message(message):
        request.node.error_message = message
    request.node.add_error_message = _add_error_message


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Test Case Description</th>")
    cells.insert(2, "<th>Form Type</th>")
    cells.insert(3, "<th>Form Page</th>")
    cells.insert(4, "<th>Error message</th>")
    cells.insert(5, "<th>Lead status</th>")
    cells.pop(-1)
    cells.pop(-1)
    cells.pop(-1)


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(1, f"<td>{getattr(report, 'test_case', 'Тест не завершен')}</td>")
    cells.insert(2, f"<td>{getattr(report, 'form_type', 'N/A')}</td>")
    cells.insert(3, f"<td>{getattr(report, 'form_page', 'N/A')}</td>")
    cells.insert(4, f"<td>{report.error_message}</td>")
    lead_status = getattr(report, 'check_leads_result', 'Не проверялось, тк форма не отправилась')
    status_color = 'green' if lead_status == 'PASSED' else 'red' if lead_status == 'FAILED' else 'gray'
    cells.insert(5, f'<td style="color:{status_color}">{lead_status}</td>')
    cells.pop(-1)
    cells.pop(-1)
    cells.pop(-1)

    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.test_case = getattr(item, 'test_case', item.name)
    report.form_page = getattr(item, 'form_page', '')
    report.form_type = getattr(item, 'form_type', '')
    report.error_message = getattr(item, 'error_message', '')
    report.check_leads_result = getattr(item, 'check_leads_result')
    
    
