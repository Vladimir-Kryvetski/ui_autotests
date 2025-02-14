import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from classes.classes_form import Locators, GenericForm, Bitrix24
import time


@pytest.mark.parametrize("form_type, test_data, url, expected_texts", [
    ('p100', ('все поля заполнены', 'Форма П100', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support', ['Спасибо за заявку!']),
    ('p100', ('только обязательные заполнены', 'Форма П100', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/', ['Спасибо за заявку!']),
    ('p20', ('все поля заполнены', 'Форма П20', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support', ['Спасибо за заявку!']),
    ('p20', ('только обязательные заполнены', 'Форма П20', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/', ['Спасибо за заявку!']),
    ('p50', ('все поля заполнены', 'Форма П50', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support', ['Спасибо за заявку!']),
    ('p50', ('только обязательные заполнены', 'Форма П50', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/', ['Спасибо за заявку!']),
    ('p10', ('все поля заполнены', 'Форма П10', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support', ['Спасибо за заявку!']),
    ('p10', ('только обязательные заполнены', 'Форма П10', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/', ['Спасибо за заявку!']),
    ('all_in', ('только обязательные заполнены', 'Форма all_in', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('all_in', ('все поля заполнены', 'Форма all_in', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('front_back_seo', ('только обязательные заполнены', 'Форма front_back_seo', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('front_back_seo', ('все поля заполнены', 'Форма front_back_seo', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('front_back_safe', ('только обязательные заполнены', 'Форма front_back_safe', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('front_back_safe', ('все поля заполнены', 'Форма front_back_safe', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('back_safe', ('только обязательные заполнены', 'Форма back_safe', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('back_safe', ('все поля заполнены', 'Форма back_safe', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('forma_13', ('все поля заполнены', 'Форма_13', None, '+375(12)345-67-8', None, None), 'https://manao-team.com/services/audit/', ['Спасибо за заявку!']),
    ('forma1', ('только обязательные заполнены', 'Форма1', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/', ['Спасибо за заявку!']),
    ('forma1', ('все поля заполнены', 'Форма1', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/', ['Спасибо за заявку!']),
    ('forma2', ('только обязательные заполнены', 'Форма2', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/support/', ['Спасибо за заявку!']),
    ('forma2', ('все поля заполнены', 'Форма2', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support/', ['Спасибо за заявку!']),
    ('forma3', ('все поля заполнены', 'Форма3', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/support/', ['Спасибо за заявку!']),
    ('forma4', ('только обязательные заполнены', 'Форма4', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/', ['Спасибо за заявку!']),
    ('forma4', ('все поля заполнены', 'Форма4', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/', ['Спасибо за заявку!']),
    ('forma5', ('все поля заполнены', 'Форма5', 'proverka@gmail.com', None, None, None),'https://manao-team.com/publications/rasskazyvaem-pochemu-sayt-ne-prinosit-pribyl-i-darim-chek-list/', ['Всё отправили на вашу почту, можете проверять!']),
    ('forma6', ('только обязательные заполнены', 'Форма6', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/publications/chto-takoe-ux-audit-sayta-i-kak-my-ego-provodim/', ['Спасибо за заявку!']),
    ('forma6', ('все поля заполнены', 'Форма6', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/publications/chto-takoe-ux-audit-sayta-i-kak-my-ego-provodim/', ['Спасибо за заявку!']),
    ('forma7', ('все поля заполнены', 'forma7', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/audit-design/', ['Спасибо за заявку!']),
    ('forma7', ('только обязательные заполнены', 'forma7', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/audit-design/', ['Спасибо за заявку!']),
    ('forma8', ('все поля заполнены', 'forma8', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/website-improvement/', ['Спасибо за заявку!']),
    ('forma8', ('только обязательные заполнены', 'forma8', 'proverka@gmail.com', '+375(12)345-67-8', None,'autotest'), 'https://manao-team.com/services/website-improvement/', ['Спасибо за заявку!']),
    ('forma_internet_shop', ('все поля заполнены', 'forma_internet_shop', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop/', ['Спасибо за заявку!']),
    ('forma_internet_shop', ('только обязательные заполнены', 'forma_internet_shop', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop/', ['Спасибо за заявку!']),
    ('forma_corporate_site', ('все поля заполнены', 'forma_corporate_site', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop/', ['Спасибо за заявку!']),
    ('forma_corporate_site', ('только обязательные заполнены', 'forma_corporate_site', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop/',['Спасибо за заявку!']),
    ('forma_site_gotovoe_reshenie', ('все поля заполнены', 'forma_site_gotovoe_reshenie', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop/', ['Спасибо за заявку!']),
    ('forma_site_gotovoe_reshenie', ('только обязательные заполнены', 'forma_site_gotovoe_reshenie', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop/',
    ['Спасибо за заявку!']),
    ('forma_landing', ('все поля заполнены', 'forma_landing', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop/', ['Спасибо за заявку!']),
    ('forma_landing', ('только обязательные заполнены', 'forma_landing', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop/',['Спасибо за заявку!']),
    ('forma_catalog', ('все поля заполнены', 'forma_catalog', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop/', 
    ['Спасибо за заявку!']),
    ('forma_catalog', ('только обязательные заполнены', 'forma_catalog', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop/',['Спасибо за заявку!']),
    ('forma_9', ('все поля заполнены', 'forma_9', None, '+375(12)345-67-8', None, None),'https://manao-team.com/services/develop/', 
    ['Спасибо за заявку!']),
    ('forma_10', ('все поля заполнены', 'forma_10', None, '+375(12)345-67-8', None, None),'https://manao-team.com/services/develop-shop/', 
    ['Спасибо за заявку!']),
    ('forma_pod_kluch', ('все поля заполнены', 'forma_pod_kluch', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-shop/', 
    ['Спасибо за заявку!']),
    ('forma_pod_kluch', ('только обязательные заполнены', 'forma_pod_kluch', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-shop/',['Спасибо за заявку!']),
    ('forma_gotovoe_reshenie', ('все поля заполнены', 'forma_gotovoe_reshenie', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-shop/', ['Спасибо за заявку!']),
    ('forma_gotovoe_reshenie', ('только обязательные заполнены', 'forma_gotovoe_reshenie', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-shop/',['Спасибо за заявку!']),
    ('forma_korporotive_site_3.0', ('все поля заполнены', 'forma_korporotive_site_3.0', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-on-templates/', ['Спасибо за заявку!']),
    ('forma_korporotive_site_3.0', ('только обязательные заполнены', 'forma_korporotive_site_3.0', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-on-templates/',['Спасибо за заявку!']),
    ('forma_lite_shop', ('все поля заполнены', 'forma_lite_shop', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-on-templates/', ['Спасибо за заявку!']),
    ('forma_lite_shop', ('только обязательные заполнены', 'forma_lite_shop', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-on-templates/',['Спасибо за заявку!']),
    ('forma_intec_prom', ('все поля заполнены', 'forma_intec_prom', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-on-templates/', ['Спасибо за заявку!']),
    ('forma_intec_prom', ('только обязательные заполнены', 'forma_intec_prom', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-on-templates/',
    ['Спасибо за заявку!']),
    ('forma_intec_universe', ('все поля заполнены', 'forma_intec_universe', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-on-templates/', ['Спасибо за заявку!']),
    ('forma_intec_universe', ('только обязательные заполнены', 'forma_intec_universe', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-on-templates/',
    ['Спасибо за заявку!']),
    ('forma_focus', ('все поля заполнены', 'forma_focus', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-on-templates/', ['Спасибо за заявку!']),
    ('forma_focus', ('только обязательные заполнены', 'forma_focus', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-on-templates/',
    ['Спасибо за заявку!']),
    ('forma_s_nulya', ('все поля заполнены', 'forma_s_nulya', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-corporate/', ['Спасибо за заявку!']),
    ('forma_s_nulya', ('только обязательные заполнены', 'forma_s_nulya', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-corporate/',
    ['Спасибо за заявку!']),
    ('forma_na_gotovom', ('все поля заполнены', 'forma_na_gotovom', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/develop-corporate/', ['Спасибо за заявку!']),
    ('forma_na_gotovom', ('только обязательные заполнены', 'forma_na_gotovom', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/develop-corporate/',
    ['Спасибо за заявку!']),
    ('forma_11', ('все поля заполнены', 'forma_11', None, '+375(12)345-67-8', None, None),'https://manao-team.com/services/develop-corporate/', 
    ['Спасибо за заявку!']),
    ('forma_12', ('все поля заполнены', 'forma_12', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/design/', ['Спасибо за заявку!']),
    ('forma_12', ('только обязательные заполнены', 'forma_12', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/design/',
    ['Спасибо за заявку!']),
    ('forma_korporotive_site', ('все поля заполнены', 'forma_korporotive_site', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/design/', ['Спасибо за заявку!']),
    ('forma_korporotive_site', ('только обязательные заполнены', 'forma_korporotive_site', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/design/',
    ['Спасибо за заявку!']),
    ('forma_internet_magaz', ('все поля заполнены', 'forma_internet_magaz', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),'https://manao-team.com/services/design/', ['Спасибо за заявку!']),
    ('forma_internet_magaz', ('только обязательные заполнены', 'forma_internet_magaz', 'proverka@gmail.com', None, None, None), 'https://manao-team.com/services/design/',
    ['Спасибо за заявку!']),
])

@pytest.mark.webforms
def test_webforms(form_type, test_data, url, page: Page, request,  expected_texts):
    (test_case, name, email, phone, site, comments) = test_data
    request.node.form_type = form_type
    request.node.form_page = url
    request.node.test_case = test_case
    request.node.test_data = test_data

    #Определение локаторов в зависимости от типы формы
    locators = Locators.forms[form_type]

    #Создание формы
    form = GenericForm(page, locators)

    try:
        form.open_page(url)
        form.close_modal_if_present()
        form.fill_form(name, email, phone, site, comments)
        form.submit_form()
        form.check_success_message(expected_texts)

    except Exception as e:
        request.node.add_error_message(str(e))
        pytest.fail(str(e), pytrace=False)

@pytest.mark.integration
def test_check_all_leads(webhook_url, request):
    load_dotenv()
    time.sleep(5)

    try:
        if not webhook_url:
            raise Exception('Webhook url is not found in env variables')
    
        bitrix = Bitrix24(webhook_url)

        bitrix.get_leads()
        test_data = request.node.test_data
        lead_created = bitrix.check_leads(test_data[1])
        request.node.check_leads_result = 'PASSED' if lead_created else 'FAILED'

        if not lead_created:
            raise Exception('Lead is not created in Bitrix24')

    except Exception as e:
        request.node.check_leads_result = 'FAILED'
    


    
    
    

    
    

    
    
 





    



    
    
