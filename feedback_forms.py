from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from locators import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://manao-team.com/")
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

def test_form_leave_request_reqiured_fields_filled(driver, wait):
    name_field_element = wait.until(EC.presence_of_element_located((By.XPATH, name_leave_request_embedded)))
    driver.execute_script("arguments[0].scrollIntoView(true);", name_field_element)
    name_field_element.send_keys('TestName')
    email_field_element = wait.until(EC.presence_of_element_located((By.XPATH, email_leave_request_embedded)))
    email_field_element.send_keys('testmanao@gmail.com')
    sbm_btn_element = wait.until(EC.presence_of_element_located((By.XPATH, sbt_btn_leave_request_embedded)))
    sbm_btn_element.click()
    success_elem = wait.until(EC.presence_of_element_located((By.XPATH, success_text_leave_request_embedded)))
    wait.until(EC.url_changes("https://manao-team.com/"))
    assert success_elem.is_displayed(), "Элемент success_elem не найден на новой странице"

def test_form_leave_request_reqiured_all_fields_filled(driver, wait):
    name_field_element = wait.until(EC.presence_of_element_located((By.XPATH, name_leave_request_embedded)))
    driver.execute_script("arguments[0].scrollIntoView(true);", name_field_element)
    name_field_element.send_keys('TestName')
    email_field_element = wait.until(EC.presence_of_element_located((By.XPATH, email_leave_request_embedded)))
    email_field_element.send_keys('testmanao@gmail.com')
    site_field_element = wait.until(EC.presence_of_element_located((By.XPATH, site_field_leave_request_embedded)))
    site_field_element.send_keys('https://example.com/')
    details_field_element = wait.until(EC.presence_of_element_located((By.XPATH, details_leave_request_embedded)))
    details_field_element.send_keys('https://example.com/')
    sbm_btn_element = wait.until(EC.presence_of_element_located((By.XPATH, sbt_btn_leave_request_embedded)))
    sbm_btn_element.click()
    success_elem = wait.until(EC.presence_of_element_located((By.XPATH, success_text_leave_request_embedded)))
    wait.until(EC.url_changes("https://manao-team.com/"))
    assert success_elem.is_displayed(), "Элемент success_elem не найден на новой странице"

def test_form_leave_request_empty_name(driver, wait):
    original_url = driver.current_url
    name_field_element = wait.until(EC.presence_of_element_located((By.XPATH, name_leave_request_embedded)))
    driver.execute_script("arguments[0].scrollIntoView(true);", name_field_element)
    name_field_element.send_keys('')
    email_field_element = wait.until(EC.presence_of_element_located((By.XPATH, email_leave_request_embedded)))
    email_field_element.send_keys('testmanao@gmail.com')
    sbm_btn_element = wait.until(EC.presence_of_element_located((By.XPATH, sbt_btn_leave_request_embedded)))
    sbm_btn_element.click()
    assert driver.current_url == original_url, "URL не должен изменяться"

    

















    
    
    
    
    

    
   
   
   
   
   
   

   


  
    