1  установки зависимостей использовать команду:
pip install -r requirements.txt

2 Для запуска всех тестов из файла:
pytest имя_файла
Пример
pytest feedback_forms.py

3 Для запуска выбранного теста из файла:
pytest имя_файла::название_теста(функции)
Пример
pytest feedback_forms.py::test_form_leave_request_empty_name

4 Для запуска выбранного теста с генерацией html отчета:

Пример

pytest --html=report.html feedback_forms.py::test_form_leave_request_empty_name
