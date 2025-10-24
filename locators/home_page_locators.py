from selenium.webdriver.common.by import By

class HomePageLocators:
    # Разделы ингредиентов
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']/parent::div")
    
    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_NAME = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_name__')]")
    INGREDIENT_PRICE = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_price__')]")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__1S7dV")
    INGREDIENT_BUN = (By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']/parent::a")
    INGREDIENT_SAUCE = (By.XPATH, ".//p[text() = 'Соус Spicy-X']/parent::a")
    INGREDIENT_FILLING = (By.XPATH, ".//p[text() = 'Мясо бессмертных моллюсков Protostomia']/parent::a")
    INGREDIENT_COUNTER_BUN = (By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']/parent::a/div[@class = 'counter_counter__ZNLkj counter_default__28sqi']/p")
    
    # Конструктор бургера
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
    BUN_TOP_SLOT = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_bunPositionTop__')]")
    BUN_BOTTOM_SLOT = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_bunPositionBottom__')]")
    FILLINGS_SLOT = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_ingredients__')]")
    
    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    
    # Модальные окна
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_overlay__')]")
    
    # Детали заказа в модальном окне
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2[contains(@class, 'text_type_digits-large')]")
    ORDER_SUCCESS_TEXT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//p[contains(text(), 'идентификатор заказа')]")

    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
