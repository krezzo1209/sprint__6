from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(),'Заказать') and contains(@class,'top')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(),'Заказать') and contains(@class,'bottom')]")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex")

    QUESTIONS_TOGGLES = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
    ]

    QUESTIONS_TEXTS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
    ]

    def open(self):
        self.open_url(self.URL)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def click_order_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.click(self.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)

    def get_question_answer(self, index):
        toggle_locator = self.QUESTIONS_TOGGLES[index]
        answer_locator = self.QUESTIONS_TEXTS[index]

        self.wait_for_element(toggle_locator)
        self.click(toggle_locator)


        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(answer_locator))
        return self.f

