import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By
from locators.ingredient_modal_locators import IngredientModalLocators

class HomePage(BasePage):
    
    @allure.step('Кликнуть на раздел "Конструктор"')
    def click_constructor(self):
        self.click_element(BasePageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step('Кликнуть на раздел "Лента Заказов"')
    def click_order_feed(self):
        self.click_element(BasePageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        # Удаляем параметр ingredient_index и используем фиксированный ингредиент
        ingredient = self.find_element(HomePageLocators.INGREDIENT_ITEM)[0]
        ingredient.click()
    
    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click_element(HomePageLocators.MODAL_CLOSE)

    @allure.step('Добавить булочку в заказ')
    def add_bun(self):
        ingredient = self.wait_for_element(HomePageLocators.INGREDIENT_BUN)
        constructor = self.wait_for_element(HomePageLocators.BURGER_CONSTRUCTOR)
        
        # Drag and drop ингредиента в конструктор
        self.drag_and_drop_element(ingredient, constructor)

    @allure.step('Добавить соус в заказ')
    def add_sauce(self):
        ingredient = self.wait_for_element(HomePageLocators.INGREDIENT_SAUCE)
        constructor = self.wait_for_element(HomePageLocators.BURGER_CONSTRUCTOR)
        
        # Drag and drop ингредиента в конструктор
        self.drag_and_drop_element(ingredient, constructor)

    @allure.step('Добавить начинку в заказ')
    def add_filling(self):
        ingredient = self.wait_for_element(HomePageLocators.INGREDIENT_FILLING)
        constructor = self.wait_for_element(HomePageLocators.BURGER_CONSTRUCTOR)
        
        # Drag and drop ингредиента в конструктор
        self.drag_and_drop_element(ingredient, constructor)

    @allure.step('Получить счетчик ингредиента')
    def get_ingredient_counter(self):
        self.wait_for_element(HomePageLocators.INGREDIENT_COUNTER_BUN)
        return self.get_text(HomePageLocators.INGREDIENT_COUNTER_BUN)
    
    @allure.step('Проверить невидимости модального окна')
    def is_modal_invisible(self):
        return self.wait_for_element_hide(HomePageLocators.MODAL)
    
    @allure.step('Проверить видимости модального окна')
    def is_modal_visible(self):
        return self.wait_for_element(HomePageLocators.MODAL)

    @allure.step('Получить детали ингредиента из модального окна')
    def get_ingredient_details(self):
        return {
            'name': self.get_text(IngredientModalLocators.INGREDIENT_NAME),
            'image': self.is_element_visible(IngredientModalLocators.INGREDIENT_IMAGE),
            'nutrition': self.get_text(IngredientModalLocators.NUTRITION_FACTS)
        }
    
    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_make_order(self):
        """Клик по кнопке оформления заказа"""
        self.click_element(HomePageLocators.ORDER_BUTTON)
    
    @allure.step('Ожидать появление модального окна заказа')
    def wait_for_order_modal(self, timeout=10):
        """Ожидание появления модального окна с заказом"""
        return self.wait_for_element(HomePageLocators.MODAL, timeout)
    
    @allure.step('Получить номер заказа из модального окна')
    def get_order_number(self):
        """Получение номера заказа из модального окна"""
        try:
            order_number_element = self.wait_for_element(HomePageLocators.ORDER_NUMBER, timeout=5)
            return order_number_element.text
        except:
            # Альтернативный способ поиска номера заказа
            modal = self.wait_for_element(HomePageLocators.MODAL)
            elements = modal.find_elements(By.TAG_NAME, "p")
            for element in elements:
                text = element.text
                if text.isdigit() and len(text) > 3:
                    return text
            return None
    
    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):
        """Закрытие модального окна заказа"""
        self.click_element(HomePageLocators.MODAL_CLOSE)
    
    @allure.step('Проверить, что заказ можно оформить')
    def can_make_order(self):
        """Проверка активности кнопки оформления заказа"""
        order_button = self.wait_for_element(HomePageLocators.ORDER_BUTTON)
        return order_button.is_enabled()
    
    @allure.step('Проверить наличие добавленных ингредиентов')
    def has_ingredients_in_constructor(self):
        """Проверка, что в конструкторе есть ингредиенты"""
        try:
            fillings = self.find_element(HomePageLocators.FILLINGS_SLOT)
            return len(fillings) > 0
        except:
            return False
        
    
    @allure.step('Нажать на кнопку "Войти в аккаунт')
    def click_login_button(self):   
        self.click_element(HomePageLocators.LOGIN_BUTTON)
    
    @allure.step('Ожидать загрузку кнопки "Оформить заказ')
    def wait_for_button_make_order(self, timeout=10):
        """Ожидание загрузки кнопки"""
        return self.wait_for_element(HomePageLocators.ORDER_BUTTON, timeout)
    