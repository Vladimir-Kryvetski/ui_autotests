from typing import Dict, Optional
from abc import ABC, abstractmethod
from playwright.sync_api import Page, TimeoutError, ElementHandle
import pytest
import requests
from .locators import Locators
from dotenv import load_dotenv


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

    def close_modal_if_present(self):
        try:
            model_close_btn = self.page.locator('.fancybox-close-small')
            if model_close_btn.is_visible:
                model_close_btn.click()
        except TimeoutError as e:
             print(f"Модальное окно не появилось: {e}")
        except ElementHandle as e:
            print(f"Ошибка при работе с элементом модального окна {e}")

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

    def check_success_message(self, expected_texts):
        actual_text = self.page.locator(self.locators['success_text']).inner_text()
        error_message = (
            f"Текст успешного сообщения не совпадает на странице {self.page.url}:\n"
            f"ожидается текст {expected_texts}\n"
            f"получен {actual_text}"
        )
        assert actual_text in expected_texts, error_message

load_dotenv()

class Bitrix24(GenericForm):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.response_data = None
        self.check_leads_result = None

    def get_leads(self):
        try:
            response = requests.get(self.webhook_url)
            response.raise_for_status()
            self.response_data = response.json()
            return self.response_data
        except requests.exceptions.RequestException as e:
            self.check_leads_result = False
            raise Exception(f'Failed to get leads from Bitrix24, {str(e)}')

    def check_leads(self, name : str):
        if not self.response_data:
            self.check_leads_result = False
            return False
        
        if 'result' in self.response_data:
            leads = self.response_data
            for lead in leads:
                if lead.get('NAME') == name:
                    self.check_leads_result = True
                    return True
            self.check_leads_result = False
            return False
        else:
            self.check_leads_result = False
            return False
            

        
        
        
        
        
        
        
        
        
        
        
        
        































        

















































