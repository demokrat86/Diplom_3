from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL = (By.XPATH, './/input[@type="text"]')
    PASSWORD = (By.XPATH, './/input[@type="password"]')
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")
