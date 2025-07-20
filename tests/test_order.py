# tests/test_order.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import order_test_data


@pytest.mark.parametrize("order_data", order_test_data)
@pytest.mark.parametrize("entry_point", ["top", "bottom"])
def test_order_creation(driver, order_data, entry_point):
    """Тест создания заказа через разные точки входа"""
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open()

    if entry_point == "top":
        main_page.click_order_top()
    else:
        main_page.click_order_bottom()

    order_page.fill_form(**order_data)
    order_page.submit_order()

    message = order_page.get_success_message()
    assert "успешно создан" in message.lower(), f"Сообщение: {message}"


def test_scooter_logo_redirect(driver):
    """Тест перехода на главную страницу через логотип Самоката"""
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_logo_scooter()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


def test_yandex_logo_redirect(driver):
    """Тест перехода на Dzen через логотип Яндекса"""
    main_page = MainPage(driver)
    main_page.open()
    
    main_window_handle = driver.current_window_handle
    main_page.click_logo_yandex()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    new_window_handle = [h for h in driver.window_handles if h != main_window_handle][0]
    driver.switch_to.window(new_window_handle)

    assert any(domain in driver.current_url for domain in ['dzen.ru', 'zen.yandex'])
    
    driver.close()
    driver.switch_to.window(main_window_handle)
