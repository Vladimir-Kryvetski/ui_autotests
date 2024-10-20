from abc import ABC, abstractmethod
from playwright.sync_api import Page, expect


class Locators:

    submit_application_locators = {
        "name_field": "//input[@name = 'form_text_1']",
        "phone_field": "//input[@name = 'form_text_2']",
        "email_field": "//input[@name = 'form_email_3']",
        "details_field": "//textarea[@name = 'form_textarea_5']",
        "submit_btn": "//button[@name='web_form_submit']",
        "site_field": "//input[@name = 'form_text_14']",
        "success_text": "//h1[text() ='Спасибо за заявку!']",
    }

    form_p100 = {
        "form_btn": "//a[@data-form = 'Пакет 100']",
        "form_name": "//input[@value='Пакет 100']/following::label[1]/input[@name = 'form_text_1']",
        "form_phone": "//input[@value='Пакет 100']/following::label[2]/input[@name = 'form_text_2']",
        "form_email": "//input[@value='Пакет 100']/following::label[3]/input[@name = 'form_email_3']",
        "form_site": "//input[@value='Пакет 100']/following::label[4]/input[@name = 'form_text_14']",
        "form_comments": "//input[@value='Пакет 100']/following::label[5]/textarea[@name = 'form_textarea_5']",
        "form_sbt_btn": "//input[@value='Пакет 100']/following::div[2]/following::button[1]",
        "success_text": "//h1[text() ='Спасибо за заявку!']",
    }


class BaseForm(ABC):
    def __init__(self, page: Page, locators: Locators):
        self.page = page
        self.locators = locators

    @abstractmethod
    def fill_form(self):
        pass

    @abstractmethod
    def submit_form(self):
        pass

    @abstractmethod
    def check_success_message(self):
        pass


class SubmitApplication(BaseForm):
    def __init__(self, page, locators):
        super().__init__(page, locators)
        self.form_name = ''
        self.form_url = ''

    # None for not required fields    
    def fill_form(self, name, email, phone=None, site=None, comments=None):
        self.form_name = name
        self.form_url = self.page.url
        self.page.locator(Locators.submit_application_locators['name_field']).first.fill(name)
        self.page.locator(Locators.submit_application_locators['email_field']).first.fill(email)
        if phone:
            self.page.locator(Locators.submit_application_locators['phone_field']).first.fill(phone)
        if site:
            self.page.locator(Locators.submit_application_locators['site_field']).first.fill(site)
        if comments:
            self.page.locator(Locators.submit_application_locators['details_field']).first.fill(comments)

    def submit_form(self):
        self.page.locator(Locators.submit_application_locators['submit_btn']).first.click()

    def check_success_message(self, expected_text):
        try:
            actual_text = self.page.locator(Locators.submit_application_locators['success_text']).inner_text()
            error_message = (
                f"Текст успешного сообщения не совпадает:\n"
                f"ожидается текст {expected_text}\n"
                f"получен {actual_text}"
        )
            assert actual_text == expected_text, error_message
        except AssertionError as e:
            raise AssertionError(f"Тест провален {str(e)}")

    def check_url(self, base_url):
        actual_url = self.page.url
        error_text = f"URL изменился стал {actual_url} , а должен быть {base_url}"
        expect((self.page), error_text).to_have_url(base_url)


class FormP100(BaseForm):
    def __init__(self, page, locators):
        super().__init__(page, locators)
        self.form_name = ''
        self.form_url = ''

    def open_page(self, url):
        self.page.goto(url)

    def fill_form(self, name, email, phone=None, site=None, comments=None):
        self.form_name = name
        self.form_url = self.page.url
        self.page.locator(Locators.form_p100['form_btn']).click()
        self.page.locator(Locators.form_p100['form_name']).fill(name)
        self.page.locator(Locators.form_p100['form_email']).fill(email)
        if phone:
            self.page.locator(Locators.form_p100['form_phone']).fill(phone)
        if site:
            self.page.locator(Locators.form_p100['form_site']).fill(site)
        if comments:
            self.page.locator(Locators.form_p100['form_comments']).fill(comments)

    def submit_form(self):
        self.page.locator(Locators.form_p100['form_sbt_btn']).click()

    def check_success_message(self, expected_text):
        actual_text = self.page.locator(Locators.form_p100['success_text']).inner_text()
        error_message = (
            f"Текст успешного сообщения не совпадает:\n"
            f"ожидается текст {expected_text}\n"
            f"получен {actual_text}"
        )
        assert actual_text == expected_text, error_message


