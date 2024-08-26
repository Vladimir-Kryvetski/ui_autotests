import pytest
from playwright.sync_api import Page, expect


class Locators:
    name_field = "//input[@name = 'form_text_1']"
    phone_field = "//input[@name = 'form_text_2']"
    email_field = "//input[@name = 'form_email_3']"
    details_field = "//textarea[@name = 'form_textarea_5'][1]"
    submit_btn = "//button[@name='web_form_submit'][1]"
    site_field = "//input[@name = 'form_text_14'][1]"
    success_text = "//h1[text() ='Спасибо за заявку!']"

@pytest.mark.positive
def test_form_all_fields_filled(page: Page):
    page.query_selector(Locators.name_field).fill('Форма П10')
    page.query_selector(Locators.email_field).fill('proverka@gmail.com')
    page.query_selector(Locators.phone_field).fill('+375(12)345-67-8')
    page.query_selector(Locators.site_field).fill('test.test')
    page.query_selector(Locators.details_field).fill('autotest')
    page.query_selector(Locators.submit_btn).click()
    expect(page.locator(Locators.success_text),"Текст успешного сообщения не совпадает").to_have_text('Спасибо за заявку!')

@pytest.mark.positive
def test_form_only_required_fields_filled(page: Page):
    page.query_selector(Locators.name_field).fill('Форма П10')
    page.query_selector(Locators.email_field).fill('proverka@gmail.com')
    page.query_selector(Locators.submit_btn).click()
    expect(page.locator(Locators.success_text),"Текст успешного сообщения не совпадает").to_have_text('Спасибо за заявку!')   

@pytest.mark.negative  
def test_form_empty_name(page: Page, setup_tests):
    base_url = setup_tests
    page.query_selector(Locators.name_field).fill('')
    page.query_selector(Locators.email_field).fill('proverka@gmail.com')
    page.query_selector(Locators.phone_field).fill('+375(12)345-67-8')
    page.query_selector(Locators.site_field).fill('test.test')
    page.query_selector(Locators.details_field).fill('autotest')
    page.query_selector(Locators.submit_btn).click()
    expect((page),"Пользователь зарегистриован с недействительными данными").to_have_url(base_url)

