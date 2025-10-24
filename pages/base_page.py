import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Ожидание элемента {locator}')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Клик на элемент")
    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        try:
            element.click()
        except ElementClickInterceptedException:
        # Если перекрыт, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step('Получение текста элемента {locator}')
    def get_text(self, locator):
        return self.wait_for_element(locator).text
    
    @allure.step('Скролл к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Проверка видимости элемента {locator}')
    def is_element_visible(self, locator, timeout=5):
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False

    @allure.step('Ожидание что элемент пропал')
    def wait_for_element_hide(self, locator):
        try:
            WebDriverWait(self.driver, timeout=10).until(
            EC.invisibility_of_element_located(locator)
        )
            return True
        except:
            return False
    
    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)
    
    @allure.step("Заполнение поля")
    def send_keys_to_input(self, locator, keys):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(keys)
        