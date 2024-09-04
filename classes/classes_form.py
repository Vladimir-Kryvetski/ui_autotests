from abc import ABC, abstractmethod
from playwright.sync_api import Page, expect


class Locators:

    submit_application_locators = {
        "name_field" : "//input[@name = 'form_text_1']",
        "phone_field" : "//input[@name = 'form_text_2']",
        "email_field" : "//input[@name = 'form_email_3']",
        "details_field" : "//textarea[@name = 'form_textarea_5'][1]",
        "submit_btn" : "//button[@name='web_form_submit'][1]",
        "site_field" : "//input[@name = 'form_text_14'][1]",
        "success_text" : "//h1[text() ='Спасибо за заявку!']",
    }


class BaseForm(ABC):
    def __init__(self, page:Page, locators:Locators):
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

    # None for not required fields    
    def fill_form(self, name, email, phone=None, site=None, comments=None):
        self.page.query_selector(Locators.submit_application_locators['name_field']).fill(name)
        self.page.query_selector(Locators.submit_application_locators['email_field']).fill(email)
        if phone:
            self.page.query_selector(Locators.submit_application_locators['phone_field']).fill(phone)
        if site:
            self.page.query_selector(Locators.submit_application_locators['site_field']).fill(site)
        if comments:
            self.page.query_selector(Locators.submit_application_locators['details_field']).fill(comments)

    def submit_form(self):
        self.page.query_selector(Locators.submit_application_locators['submit_btn']).click()

    def check_success_message(self, expected_text):
        actual_text = self.page.locator(Locators.submit_application_locators['success_text']).inner_text()
        error_message = (
            f"Текст успешного сообщения не совпадает:\n" 
            f"ожидается текст {expected_text}\n"
            f"получен {actual_text}"
            )
        assert actual_text == expected_text, error_message

    def check_url(self, base_url):
        actual_url = self.page.url
        error_text = f"URL изменился стал {actual_url} , а должен быть {base_url}"
        expect((self.page), error_text).to_have_url(base_url)
    
    
    
