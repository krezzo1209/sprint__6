# pages/main_page.py

from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL


class MainPage(BasePage):
    def open(self):
        self.open_url(MAIN_PAGE_URL)

    def click_order_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    def get_question_answer(self, index):
        toggle_locator = MainPageLocators.QUESTIONS_TOGGLES[index]
        answer_locator = MainPageLocators.QUESTIONS_TEXTS[index]

        self.click(toggle_locator)
        self.wait_for_element(answer_locator)
        return self.find(answer_locator).text