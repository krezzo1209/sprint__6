

from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.NAME, "name")
    SURNAME_INPUT = (By.NAME, "surname")
    ADDRESS_INPUT = (By.NAME, "address")
    PHONE_INPUT = (By.NAME, "phone")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Заказать')]")
    SUCCESS_MODAL_TITLE = (By.CLASS_NAME, "Order_Modal__title")