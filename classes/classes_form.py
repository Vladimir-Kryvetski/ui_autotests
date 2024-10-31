from typing import Dict, Optional
from abc import ABC, abstractmethod
from playwright.sync_api import Page, TimeoutError, ElementHandle
import pytest


class Locators:

    forms = {
        "p100":{
            "btn":"//a[@data-form = 'Пакет 100']",
            "fields":{
                "name":"//input[@value='Пакет 100']/following::label[1]/input[@name = 'form_text_1']",
                "phone":"//input[@value='Пакет 100']/following::label[1]/input[@name = 'form_text_1']",
                "email":"//input[@value='Пакет 100']/following::label[3]/input[@name = 'form_email_3']",
                "site":"//input[@value='Пакет 100']/following::label[4]/input[@name = 'form_text_14']",
                "comments":"//input[@value='Пакет 100']/following::label[5]/textarea[@name = 'form_textarea_5']"
            },
            "submit_btn":"//input[@value='Пакет 100']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
        "p20":{
            "btn":"//a[@data-form = 'Пакет 20']",
            "fields":{
                "name":"//input[@value='Пакет 20']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@value='Пакет 20']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@value='Пакет 20']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@value='Пакет 20']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@value='Пакет 20']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@value='Пакет 20']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
         "p50":{
            "btn":"//a[@data-form = 'Пакет 50']",
            "fields":{
                "name":"//input[@value='Пакет 50']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@value='Пакет 50']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@value='Пакет 50']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@value='Пакет 50']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@value='Пакет 50']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@value='Пакет 50']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
        "p10":{
            "btn":"//a[@data-form = 'Пакет 10']",
            "fields":{
                "name":"//input[@value='Пакет 10']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@value='Пакет 10']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@value='Пакет 10']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@value='Пакет 10']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@value='Пакет 10']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@value='Пакет 10']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
        "all_in":{
            "btn":"//a[@data-form = 'ALL IN']",
            "fields":{
                "name":"//input[@value='ALL IN']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@value='ALL IN']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@value='ALL IN']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@value='ALL IN']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@value='ALL IN']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@value='ALL IN']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
        "front_back_seo":{
            "btn":"//a[@data-form = 'FRONT + BACK + SEO']",
            "fields":{
                "name":"//input[@value='FRONT + BACK + SEO']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@value='FRONT + BACK + SEO']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@value='FRONT + BACK + SEO']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@value='FRONT + BACK + SEO']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@value='FRONT + BACK + SEO']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@value='FRONT + BACK + SEO']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
        "front_back_safe":{
            "btn":"//a[@data-form = 'FRONT + BACK + SAFE']",
            "fields":{
                "name":"//input[@value='FRONT + BACK + SAFE']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@value='FRONT + BACK + SAFE']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@value='FRONT + BACK + SAFE']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@value='FRONT + BACK + SAFE']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@value='FRONT + BACK + SAFE']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@value='FRONT + BACK + SAFE']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
         "back_safe":{
            "btn":"//a[@data-form = 'BACK + SAFE']",
            "fields":{
                "name":"//input[@value='BACK + SAFE']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@value='FBACK + SAFE']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@value='BACK + SAFE']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@value='BACK + SAFE']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@value='BACK + SAFE']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@value='BACK + SAFE']/following::div[2]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
         "forma_13":{
            "fields":{
                "name":"//input[@name = 'form_text_15']",
                "phone": "//input[@name = 'form_text_16']",
            },
            "submit_btn":"//input[@name = 'form_text_16']/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']"
        },
        "forma1":{
            "btn":"//a[@href = '#order-development']",
            "fields":{
                "name":"//input[@name = 'form_hidden_27']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@name = 'form_hidden_27']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@name = 'form_hidden_27']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@name = 'form_hidden_27']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@name = 'form_hidden_27']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@name = 'form_hidden_27']/following::label[5]/textarea[@name = 'form_textarea_5']/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']",
        },
        "forma2":{
            "btn":"//a[@data-form = 'Заказать техническую поддержку сайта']",
            "fields":{
                "name":"//input[@name = 'form_hidden_27']/following::label[1]/input[@name = 'form_text_1']",
                "phone": "//input[@name = 'form_hidden_27']/following::label[2]/input[@name = 'form_text_2']",
                "email": "//input[@name = 'form_hidden_27']/following::label[3]/input[@name = 'form_email_3']",
                "site": "//input[@name = 'form_hidden_27']/following::label[4]/input[@name = 'form_text_14']",
                "comments": "//input[@name = 'form_hidden_27']/following::label[5]/textarea[@name = 'form_textarea_5']",
            },
            "submit_btn":"//input[@name = 'form_hidden_27']/following::label[5]/textarea[@name = 'form_textarea_5']/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']",
        },
        "forma3":{
            "fields":{
                "name":"//input[@name = 'form_text_15']",
                "phone": "//input[@name = 'form_text_16']",
            },
        "submit_btn":"//input[@name = 'form_hidden_30']/following::label[2]/input[@name = 'form_text_16']/following::button[1]",
        "success_text":"//h1[text() ='Спасибо за заявку!']",
        },
        "forma4":{
            "fields":{
                "name":"//input[contains(@value, 'YToyOntzOjE4OiJDT01QT05FTlRfVEVNUExBVEUiO3M6O')]/following::input[1]",
                "phone": "//input[contains(@value, 'YToyOntzOjE4OiJDT01QT05FTlRfVEVNUExBVEUiO3M6O')]/following::input[2]",
                "email": "//input[contains(@value, 'YToyOntzOjE4OiJDT01QT05FTlRfVEVNUExBVEUiO3M6O')]/following::input[3]",
                "site": "//input[contains(@value, 'YToyOntzOjE4OiJDT01QT05FTlRfVEVNUExBVEUiO3M6O')]/following::input[4]",
                "comments": "//input[contains(@value, 'YToyOntzOjE4OiJDT01QT05FTlRfVEVNUExBVEUiO3M6O')]/following::input[5]",
            },
            "submit_btn":"//input[contains(@value, 'YToyOntzOjE4OiJDT01QT05FTlRfVEVNUExBVEUiO3M6O')]/following::button[1]",
            "success_text":"//h1[text() ='Спасибо за заявку!']",
        },
        "forma5":{
            "fields":{
                "name":"//input[@name = 'form_text_24']",
                "email": "//input[@name = 'form_email_25']",
            },
            "submit_btn":"//input[@name = 'form_email_25']/following::button[1]",
            "success_text":"//h2[text()='Всё отправили на вашу почту, можете проверять!']",
        },
    }

class BaseForm(ABC):
    def __init__(self, page: Page, locators: Dict):
        self.page = page
        self.locators = locators

    @abstractmethod
    def fill_form(self, name:str, email:str, phone:Optional[str], site:Optional[str], comments:Optional[str]):
        pass

    @abstractmethod
    def submit_form(self):
        pass

    @abstractmethod
    def check_success_message(self):
        pass


class GenericForm(BaseForm):
    def __init__(self, page, locators):
        super().__init__(page, locators)
        #cохраняем урл для вставки в отчет по тестированию
        self.form_url = ''

    def open_page(self, url):
        self.page.goto(url)

    def fill_form(self, name: str, email: Optional[str], phone: Optional[str], site: Optional[str], comments: Optional[str]):
        self.form_url = self.page.url
        try:
            if 'btn' in self.locators and self.page.locator(self.locators['btn']).is_visible():
                self.page.locator(self.locators['btn']).click()
            if name is not None:
                self.page.locator(self.locators['fields']['name']).fill(name)
            if 'email' in self.locators['fields'] and self.page.locator(self.locators['fields']['email']).is_visible():
                if email is not None:
                    self.page.locator(self.locators['fields']['email']).fill(email)
            if 'phone' in self.locators['fields'] and self.page.locator(self.locators['fields']['phone']).is_visible():
                if phone is not None:
                    self.page.locator(self.locators['fields']['phone']).fill(phone)
            if 'site' in self.locators['fields'] and self.page.locator(self.locators['fields']['site']).is_visible():
                if site is not None:
                    self.page.locator(self.locators['fields']['site']).fill(site)
            if 'comments' in self.locators['fields'] and self.page.locator(self.locators['fields']['comments']).is_visible():
                if comments is not None:
                    self.page.locator(self.locators['fields']['comments']).fill(comments)       
        except TimeoutError as e:
            error_msg = f"Превышено время ожидания {e}"
            self.page.context._request.node.add_error_message(error_msg)
        except ElementHandle as e: 
            error_msg = f"Элемент не найден {e}"
            self.page.context._request.node.add_error_message(error_msg)
        
    def submit_form(self):
        self.page.locator(self.locators['submit_btn']).click()

    def check_success_message(self, expected_text):
        actual_text = self.page.locator(self.locators['success_text']).inner_text()
        error_message = (
            f"Текст успешного сообщения не совпадает:\n"
            f"ожидается текст {expected_text}\n"
            f"получен {actual_text}"
        )
        assert actual_text == expected_text, error_message

















































