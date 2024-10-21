import pytest
from playwright.sync_api import Page
from classes.classes_form import *
from classes.classes_form import Locators


@pytest.mark.parametrize("form_class, form_type, test_data, url" ,[
    (FormP100, 'Форма п100', ('все поля заполнены', 'Форма П100', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support'),
    (FormP100, 'Форма п100', ('только обязательные заполнены', 'Форма П100', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/'),
    (FormP20, 'Форма п20', ('все поля заполнены', 'Форма П20', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support'),
    (FormP20, 'Форма п20', ('только обязательные заполнены', 'Форма П20', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/'),
])


def test_forms(form_class, form_type, test_data, url, page: Page, request):
    (test_case, name, email, phone, site, comments) = test_data
    request.node.form_type = form_type
    request.node.form_page = url
    request.node.test_case = test_case
    
    #Инициализация формы в зависимости от выбранного класса
    form = form_class(page, Locators)
    #Переход на страницу формы
    form.open_page(url)
    #Заполненеие и отправка формы
    form.fill_form(name, email, phone, site, comments)
    form.submit_form()
    form.check_success_message('Спасибо за заявку!')

    
    
    
