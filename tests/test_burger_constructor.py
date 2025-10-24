import allure
from config.urls import Urls
from pages.home_page import HomePage


@allure.feature('Конструктор бургеров')
class TestConstructor:
    """
    Тестовый класс для проверки навигации в разделах приложения «Конструктор бургеров».
    Проверяет корректность переходов в разделы:
    - «Конструктор»
    - «Лента Заказов»
    """

    @allure.title('Переход в раздел "Конструктор"')
    @allure.description(
        'Проверяет, что при клике на кнопку "Конструктор" происходит переход '
        'на соответствующую страницу с корректным URL.'
    )
    def test_navigate_to_constructor(self, setup_driver):
        """
        Тест перехода в раздел «Конструктор».

        Шаги:
        1. Инициализация HomePage
        2. Клик по кнопке перехода в «Конструктор»
        3. Проверка текущего URL

        Ожидаемый результат:
        Текущий URL совпадает с BASE_URL (без завершающего слеша).
        """
        with allure.step('Инициализация главной страницы'):
            home_page = HomePage(setup_driver)

        with allure.step('Переход в раздел "Конструктор"'):
            home_page.click_constructor()

        with allure.step('Проверка текущего URL'):
            current_url = home_page.get_current_url().rstrip('/')
            assert current_url == Urls.BASE_URL, (
                f"Ожидаемый URL: {Urls.BASE_URL}\n"
                f"Фактический URL: {current_url}\n"
                "Не удалось перейти в раздел «Конструктор»"
            )

    @allure.title('Переход в раздел "Лента Заказов"')
    @allure.description(
        'Проверяет, что при клике на кнопку "Лента Заказов" происходит переход '
        'на страницу ленты заказов с корректным URL.'
    )
    def test_navigate_to_order_feed(self, setup_driver):
        """
        Тест перехода в раздел «Лента Заказов».

        Шаги:
        1. Инициализация HomePage
        2. Клик по кнопке перехода в «Лента Заказов»
        3. Проверка текущего URL

        Ожидаемый результат:
        Текущий URL совпадает с ORDER_FEED_URL.
        """
        with allure.step('Инициализация главной страницы'):
            home_page = HomePage(setup_driver)

        with allure.step('Переход в раздел "Лента Заказов"'):
            home_page.click_order_feed()

        with allure.step('Проверка текущего URL'):
            current_url = home_page.get_current_url()
            assert current_url == Urls.ORDER_FEED_URL, (
                f"Ожидаемый URL: {Urls.ORDER_FEED_URL}\n"
                f"Фактический URL: {current_url}\n"
                "Не удалось перейти в раздел «Лента Заказов»"
            )
