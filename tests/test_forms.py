import pytest
from playwright.sync_api import Page
from classes.classes_form import FormP100
from classes.classes_form import Locators


@pytest.fixture(params=[
    ('Заполнены все поля формы', 'Форма П10', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),
    ('Заполнены только обязательные поля формы', 'Форма П10', 'proverka@gmail.com', None, None, None)
])
def positive_test_data(request):
    return request.param


@pytest.mark.positive_tests
def test_form_positive_scenarios(submit_application, positive_test_data, request):
    (test_case, name, email, phone, site, comments) = positive_test_data
    submit_application.fill_form(name, email, phone, site, comments)
    submit_application.submit_form()
    submit_application.check_success_message('Спасибо за заявку!')

    request.node.test_case = test_case
    request.node.form_name = name
    request.node.form_page = submit_application.form_url


@pytest.fixture(params=[
    ('Заполнены все поля формы', 'Форма П100', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),
    ('Заполнены только обязательные поля формы', 'Форма П100', 'proverka@gmail.com', None, None, None)
])
def positive_test_data(request):
    return request.param


@pytest.mark.positive_tests_1
def test_formP100(request, positive_test_data, page: Page):
    (test_case, name, email, phone, site, comments) = positive_test_data
    form_p100 = FormP100(page, Locators)
    form_p100.open_page('https://manao-team.com/services/support/')
    form_p100.fill_form(name, email, phone, site, comments)
    form_p100.submit_form()
    form_p100.check_success_message('Спасибо за заявку!')

    request.node.test_case = test_case
    request.node.form_name = name
    request.node.form_page = form_p100.form_url
