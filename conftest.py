import pytest
import requests
import json
from selenium import webdriver
from config.urls import Urls
from config.generator import generate_unique_email


@pytest.fixture(params=['chrome', 'firefox'])
def setup_driver(request):
    """
    Фикстура для инициализации веб-драйвера (Chrome или Firefox) с параметризацией.
    
    Параметры:
        request: объект запроса pytest, содержит параметр браузера ('chrome' или 'firefox')
    
    Действия:
        1. В зависимости от параметра request.param создаёт экземпляр соответствующего драйвера
        2. Открывает базовую URL-страницу приложения
        3. Разворачивает окно браузера на весь экран
        4. Возвращает драйвер для использования в тестах
        5. После завершения теста закрывает драйвер (driver.quit())
    
    Возвращает:
        Инициализированный экземпляр веб-драйвера
    """
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    
    # Открываем базовую страницу приложения
    driver.get(Urls.BASE_URL)
    # Разворачиваем окно браузера на весь экран
    driver.maximize_window()
    
    # Возвращаем драйвер в тест, после выполнения теста выполнится код после yield
    yield driver
    # Закрываем драйвер после завершения теста
    driver.quit()


@pytest.fixture
def create_and_delete_user():
    """
    Фикстура для создания тестового пользователя и его последующего удаления.
    
    Действия:
        1. Генерирует уникальный email с помощью вспомогательной функции
        2. Задаёт фиксированные значения для пароля и имени пользователя
        3. Отправляет POST-запрос на регистрацию пользователя
        4. Возвращает кортеж (email, password) для использования в тестах
        5. После выполнения теста:
            - Авторизуется под созданным пользователем
            - Получает токен доступа из ответа
            - Отправляет DELETE-запрос для удаления пользователя
    
    Возвращает:
        Кортеж (email, password) созданного пользователя
    """
    # Генерируем уникальный email для теста
    email = generate_unique_email()
    # Задаём фиксированный пароль
    password = "password123"
    # Задаём имя пользователя
    name = "Test User"
    
    # Формируем payload для регистрации пользователя
    payload = {
        'email': email, 
        'password': password, 
        'name': name
    }
    
    # Отправляем запрос на регистрацию пользователя
    requests.post(Urls.REGISTR_URL, json=payload)
        
    # Возвращаем данные пользователя в тест, после теста выполнится код после yield
    yield email, password
    
    # Формируем payload для авторизации
    payload_login = {
        'email': email, 
        'password': password, 
    }
    
    # Отправляем запрос на авторизацию
    response = requests.post(Urls.LOGIN_URL, json=payload_login)
    # Парсим JSON-ответ
    response_data = response.json()
    
    # Если в ответе есть токен доступа
    if 'accessToken' in response_data:
        # Извлекаем токен (убираем префикс 'Bearer ')
        auth_token = response_data["accessToken"][7:]
        # Формируем заголовок с авторизацией
        header = {"Authorization": auth_token}
        # Конвертируем payload в JSON-строку
        payload = json.dumps(payload)
        # Отправляем запрос на удаление пользователя
        response = requests.delete(Urls.DELETE_URL, headers=header, data=payload)
