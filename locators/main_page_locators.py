from selenium.webdriver.common.by import By

class MainPageLocators:
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