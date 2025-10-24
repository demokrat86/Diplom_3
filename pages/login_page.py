from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):

    @allure.step(f"Заполнить 'email'")
    def send_email(self, email):
        self.send_keys_to_input(LoginPageLocators.EMAIL, email)

    @allure.step(f"Заполнить 'пароль'")
    def send_password(self, password):
        self.send_keys_to_input(LoginPageLocators.PASSWORD, password)

    @allure.step(f"Нажать на кнопку 'Войти'")
    def click_login_button(self):
        self.wait_for_element(LoginPageLocators.LOGIN_BUTTON)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step(f"Авторизовать пользователя")
    def autorization(self, user):

        self.send_email(user[0])
        self.send_password(user[1])
        self.click_login_button()
