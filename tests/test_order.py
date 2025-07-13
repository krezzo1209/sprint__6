import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

test_data = [
    {"name": "Иван", "surname": "Иванов", "address": "ул. Ленина д.1", "phone": "+79991234567"},
    {"name": "Петр", "surname": "Петров", "address": "проспект Мира д.10", "phone": "+79876543210"}
]

@pytest.mark.parametrize("order_data", test_data)
def test_order_flow(driver: webdriver.Firefox, order_data):
    page = MainPage(driver)

    page.open()

    for entry_point in ["top", "bottom"]:
        if entry_point == "top":
            page.click_order_top()
        else:
            page.click_order_bottom()

        order_page = OrderPage(driver)

        order_page.fill_form(**order_data)

        order_page.submit_order()

        message = order_page.get_success_message()

        assert "успешно создан" in message.lower(), f"Сообщение: {message}"


        page.click_logo_scooter()
        assert driver.current_url == MainPage.URL


        main_window_handle = driver.current_window_handle

        page.click_logo_yandex()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

        new_window_handle = [h for h in driver.window_handles if h != main_window_handle][0]

        driver.switch_to.window(new_window_handle)

        assert 'dzen.ru' in driver.current_url or 'zen' in driver.current_url

        driver.close()

        driver.switch_to.window(main_window_handle)

