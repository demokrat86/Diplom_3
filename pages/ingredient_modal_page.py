import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators

class IngredientModalPage(BasePage):
    
    @allure.step('Получить название ингредиента в модальном окне')
    def get_ingredient_name(self):
        return self.get_text(IngredientModalLocators.INGREDIENT_NAME)
    
    @allure.step('Проверить наличие изображения ингредиента')
    def has_ingredient_image(self):
        return self.is_element_visible(IngredientModalLocators.INGREDIENT_IMAGE)
    
    @allure.step('Получить nutritional facts')
    def get_nutrition_facts(self):
        return self.get_text(IngredientModalLocators.NUTRITION_FACTS)
    