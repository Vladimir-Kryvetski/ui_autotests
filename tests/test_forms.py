import pytest


@pytest.fixture(params=[
    ('Заполнены все поля формы', 'Форма П10', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),
    ('Заполнены только обязательные поля формы','Форма П10', 'proverka@gmail.com', None, None, None)
])
def positive_test_data(request):
    return request.param

@pytest.mark.submit_application_positive_data
def test_form_positive_scenarios(submit_application, positive_test_data):
    (test_case, name, email, phone, site, comments) = positive_test_data
    submit_application.fill_form(name, email, phone, site, comments)
    submit_application.submit_form()
    submit_application.check_success_message('Спасибо за заявку!')

@pytest.fixture(params=[
    ('Отсуствует обяз. поле Имя', '', 'proverka@gmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),
    ('Отсуствует обяз. поле Почта', 'Форма П10', '', '+375(12)345-67-8', 'test.test', 'autotest'),
    ('Все поля пустые', '', '', '', '', ''),
    ('Невалидный формат почты', 'Форма П10', 'proverkagmail.com', '+375(12)345-67-8', 'test.test', 'autotest'),
])
def negative_test_data(request):
    return request.param

@pytest.mark.submit_application_negative_data
def test_form_negative_scenarios(submit_application, negative_test_data, setup_tests):
    (test_case, name, email, phone, site, comments) = negative_test_data
    submit_application.fill_form(name, email, phone, site, comments)
    submit_application.submit_form()
    submit_application.check_url(setup_tests)


    

