import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    
    @allure.step('Получить общее количество выполненных заказов')
    def get_total_orders_count(self):
        elements = self.find_element(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(elements[0].text) if elements else 0
    
    @allure.step('Получить количество выполненных заказов за сегодня')
    def get_today_orders_count(self):
        elements = self.find_element(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(elements[1].text) if len(elements) > 1 else 0
    
    @allure.step('Получить номера заказов в работе')
    def get_orders_in_progress(self):
        orders = []
        progress_section = self.wait_for_element(OrderFeedLocators.IN_PROGRESS_SECTION)
        order_elements = progress_section.find_elements(*OrderFeedLocators.IN_PROGRESS_ORDER)
        
        for order_element in order_elements:
            orders.append(order_element.text)
        
        return orders
    
    @allure.step('Проверить наличие заказа в разделе "В работе"')
    def is_order_in_progress(self, order_number):
        orders_in_progress = self.get_orders_in_progress()
        return any(str(order_number) in order for order in orders_in_progress)
    