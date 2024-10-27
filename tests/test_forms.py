import pytest
from playwright.sync_api import Page
from classes.classes_form import Locators, GenericForm


@pytest.mark.parametrize("form_type, test_data, url" ,[
    ('p100', ('все поля заполнены', 'Форма П100', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support'),
    ('p100', ('только обязательные заполнены', 'Форма П100', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/'),
    ('p20', ('все поля заполнены', 'Форма П20', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support'),
    ('p20', ('только обязательные заполнены', 'Форма П20', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/'),
    ('p50', ('все поля заполнены', 'Форма П50', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support'),
    ('p50', ('только обязательные заполнены', 'Форма П50', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/'),
    ('p10', ('все поля заполнены', 'Форма П10', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support'),
    ('p10', ('только обязательные заполнены', 'Форма П10', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/'),
    ('all_in', ('только обязательные заполнены', 'Форма all_in', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/'),
    ('all_in', ('все поля заполнены', 'Форма all_in', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/'),
    ('front_back_seo', ('только обязательные заполнены', 'Форма front_back_seo', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/'),
    ('front_back_seo', ('все поля заполнены', 'Форма front_back_seo', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/'),
    ('front_back_safe', ('только обязательные заполнены', 'Форма front_back_safe', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/'),
    ('front_back_safe', ('все поля заполнены', 'Форма front_back_safe', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/'),
    ('back_safe', ('только обязательные заполнены', 'Форма back_safe', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/'),
    ('back_safe', ('все поля заполнены', 'Форма back_safe', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/'),
    ('forma_13', ('все поля заполнены', 'Форма_13', None, '+375(12)345-67-8', None, None), 'https://manao-team.com/services/audit/'),
    ('forma1', ('только обязательные заполнены', 'Форма1', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/'),
    ('forma1', ('все поля заполнены', 'Форма1', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/'),
    ('forma2', ('только обязательные заполнены', 'Форма2', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/'),
    ('forma2', ('все поля заполнены', 'Форма2', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support/'),
    ('forma3', ('все поля заполнены', 'Форма3', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support/'),
    ('forma4', ('только обязательные заполнены', 'Форма4', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/'),
    ('forma4', ('все поля заполнены', 'Форма4', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/'),
])


def test_forms(form_type, test_data, url, page: Page, request):
    (test_case, name, email, phone, site, comments) = test_data
    request.node.form_type = form_type
    request.node.form_page = url
    request.node.test_case = test_case
    
    #Определение локаторов в зависимости от типы формы
    locators = Locators.forms[form_type]

    #Создание формы
    form = GenericForm(page, locators)

    form.open_page(url)
    form.fill_form(name, email, phone, site, comments)
    page.screenshot(path='1.png')
    form.submit_form()
    form.check_success_message('Спасибо за заявку!')

    
    
    
