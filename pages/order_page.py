from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_form(self, name="", surname="", address="", phone=""):
        self.find(OrderPageLocators.NAME_INPUT).send_keys(name)
        self.find(OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.find(OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.find(OrderPageLocators.PHONE_INPUT).send_keys(phone)

    def submit_order(self):
        self.click(OrderPageLocators.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.wait_for_element(OrderPageLocators.SUCCESS_MODAL_TITLE).text