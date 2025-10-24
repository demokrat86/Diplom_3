from selenium.webdriver.common.by import By

class BasePageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']/p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']/p[text()='Лента Заказов']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']/p[text()='Личный Кабинет']")
    