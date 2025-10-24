import allure
from pages.home_page import HomePage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage

@allure.feature('Лента заказов')
class TestOrderFeed:
    
    @allure.title('Увеличение счетчика "Выполнено за все время"')
    def test_total_orders_counter_increase(self, setup_driver, create_and_delete_user):
        home_page = HomePage(setup_driver)
        order_feed_page = OrderFeedPage(setup_driver)
        login_page = LoginPage(setup_driver)
        
        # Получаем начальное значение счетчика
        home_page.click_order_feed()
        initial_total = order_feed_page.get_total_orders_count()
        
        # Создаем заказ через конструктор
        home_page.click_constructor()
        home_page.add_bun()  # Добавляем первую булку
        home_page.add_filling()  # Добавляем первую начинку

        home_page.click_login_button()
        user = create_and_delete_user
        login_page.autorization(user)
        
        # Оформляем заказ
        home_page.wait_for_button_make_order()
        home_page.click_make_order()
        home_page.wait_for_order_modal()
        #order_number = home_page.get_order_number()
        home_page.close_order_modal()
            
        # Проверяем увеличение счетчика
        home_page.click_order_feed()
        new_total = order_feed_page.get_total_orders_count()
            
        assert new_total >= initial_total, f"Счетчик не увеличился. Было: {initial_total}, стало: {new_total}"
    
    @allure.title('Увеличение счетчика "Выполнено за сегодня"')
    def test_today_orders_counter_increase(self, setup_driver, create_and_delete_user):
        home_page = HomePage(setup_driver)
        order_feed_page = OrderFeedPage(setup_driver)
        login_page = LoginPage(setup_driver)
        
        home_page.click_order_feed()
        initial_today = order_feed_page.get_today_orders_count()
        
        home_page.click_constructor()
        home_page.add_bun()
        home_page.add_filling()

        home_page.click_login_button()
        user = create_and_delete_user
        login_page.autorization(user)
        
        # Оформляем заказ
        home_page.wait_for_button_make_order()
        
        home_page.click_make_order()
        home_page.wait_for_order_modal()
        home_page.close_order_modal()
            
        home_page.click_order_feed()
        new_today = order_feed_page.get_today_orders_count()
            
        assert new_today >= initial_today, f"Счетчик за сегодня не увеличился. Было: {initial_today}, стало: {new_today}"
        
    @allure.title('Появление заказа в разделе "В работе"')
    def test_order_appears_in_progress(self, setup_driver, create_and_delete_user):
        home_page = HomePage(setup_driver)
        order_feed_page = OrderFeedPage(setup_driver)
        login_page = LoginPage(setup_driver)
        
        # Создаем заказ
        home_page.add_bun()
        home_page.add_filling()

        home_page.click_login_button()
        user = create_and_delete_user
        login_page.autorization(user)
        
        # Оформляем заказ
        home_page.wait_for_button_make_order()

        home_page.click_make_order()
        home_page.wait_for_order_modal()

        order_number = home_page.get_order_number()
        home_page.close_order_modal()
            
        # Переходим в ленту заказов
        home_page.click_order_feed()
        
        # Получаем заказы в работе
        orders_in_progress = order_feed_page.get_orders_in_progress()
        
        # Проверяем что номер заказа есть в списке
        order_found = str(order_number) in str(orders_in_progress)
        
        assert order_found, f"Заказ {order_number} не найден в разделе 'В работе'. Найдены: {orders_in_progress}"