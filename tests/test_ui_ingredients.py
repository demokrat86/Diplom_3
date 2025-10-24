import allure
from pages.home_page import HomePage

@allure.feature('Работа с ингредиентами')
class TestIngredients:
    """
    Тестовый класс для проверки функционала работы с ингредиентами:
    - открытие/закрытие модального окна с деталями
    - изменение счётчика при добавлении ингредиента
    """

    @allure.title('Открытие модального окна с деталями ингредиента')
    @allure.description(
        'Проверяет, что при клике на ингредиент открывается модальное окно с его деталями.'
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_opening(self, setup_driver):
        """
        Тест открытия модального окна ингредиента.

        Шаги:
        1. Инициализация HomePage
        2. Клик по ингредиенту
        3. Проверка видимости модального окна

        Ожидаемый результат:
        Модальное окно отображается на экране.
        """
        with allure.step('Инициализация главной страницы'):
            home_page = HomePage(setup_driver)

        with allure.step('Клик по ингредиенту для открытия модального окна'):
            home_page.click_ingredient()

        with allure.step('Проверка видимости модального окна'):
            assert home_page.is_modal_visible(), (
                "Модальное окно не открылось. Возможно:\n"
                "- элемент не кликабелен\n"
                "- ошибка в селекторе модального окна\n"
                "- проблема с загрузкой компонента"
            )

    @allure.title('Закрытие модального окна с деталями ингредиента')
    @allure.description(
        'Проверяет, что модальное окно закрывается по клику на кнопку закрытия.'
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_modal_closing(self, setup_driver):
        """
        Тест закрытия модального окна ингредиента.

        Шаги:
        1. Инициализация HomePage
        2. Открытие модального окна (клик по ингредиенту)
        3. Закрытие модального окна
        4. Проверка скрытия модального окна

        Ожидаемый результат:
        Модальное окно исчезает с экрана.
        """
        with allure.step('Инициализация главной страницы'):
            home_page = HomePage(setup_driver)

        with allure.step('Открытие модального окна кликом по ингредиенту'):
            home_page.click_ingredient()

        with allure.step('Закрытие модального окна'):
            home_page.close_modal()

        with allure.step('Проверка скрытия модального окна'):
            assert home_page.is_modal_invisible(), (
                "Модальное окно не закрылось. Возможные причины:\n"
                "- кнопка закрытия не работает\n"
                "- ошибка в логике скрытия элемента\n"
                "- задержка в анимации закрытия"
            )

    @allure.title('Увеличение счётчика ингредиента при добавлении')
    @allure.description(
        'Проверяет, что счётчик ингредиента увеличивается при добавлении булки.'
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increase(self, setup_driver):
        """
        Тест изменения счётчика ингредиента.

        Шаги:
        1. Инициализация HomePage
        2. Получение начального значения счётчика
        3. Добавление булки
        4. Получение нового значения счётчика
        5. Сравнение значений

        Ожидаемый результат:
        Новое значение счётчика больше начального.
        """
        with allure.step('Инициализация главной страницы'):
            home_page = HomePage(setup_driver)

        with allure.step('Получение начального значения счётчика'):
            initial_counter = home_page.get_ingredient_counter()

        with allure.step('Добавление булки'):
            home_page.add_bun()

        with allure.step('Получение нового значения счётчика'):
            new_counter = home_page.get_ingredient_counter()

        with allure.step('Проверка изменения счётчика'):
            assert new_counter > initial_counter, (
                f"Счётчик не увеличился.\n"
                f"Начальное значение: {initial_counter}\n"
                f"Новое значение: {new_counter}\n"
                "Возможные причины:\n"
                "- логика добавления не работает\n"
                "- счётчик не обновляется в UI\n"
                "- ошибка в методе get_ingredient_counter()"
            )
