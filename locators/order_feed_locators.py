from selenium.webdriver.common.by import By

class OrderFeedLocators:
    # Общие счетчики заказов
    TOTAL_ORDERS_SECTION = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_SECTION = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # Статистика заказов
    ORDERS_STATS = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderStats__')]")
    
    # Лента заказов
    ORDERS_LIST = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderList__')]")
    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_orderItem__')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'OrderHistory_textBox__')]")
    
    # Заказы в работе
    IN_PROGRESS_SECTION = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__')]")
    IN_PROGRESS_ORDER = (By.XPATH, ".//li[contains(@class, 'text text_type_')]")
    
    # Общее количество заказов
    TOTAL_ORDERS_COUNT = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[1]")
    TODAY_ORDERS_COUNT = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[2]")


