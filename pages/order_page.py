from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.NAME, "name")
    SURNAME_INPUT = (By.NAME, "surname")
    ADDRESS_INPUT = (By.NAME, "address")
    PHONE_INPUT = (By.NAME, "phone")

    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Заказать')]")

    SUCCESS_MODAL_TITLE = (By.CLASS_NAME, "Order_Modal__title")  # уточняйте локатор

    def fill_form(self, name="", surname="", address="", phone=""):
        self.find(self.NAME_INPUT).send_keys(name)
        self.find(self.SURNAME_INPUT).send_keys(surname)
        self.find(self.ADDRESS_INPUT).send_keys(address)
        self.find(self.PHONE_INPUT).send_keys(phone)

    def submit_order(self):
        self.click(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MODAL_TITLE).text


