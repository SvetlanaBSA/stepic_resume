from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_PRODUCT = (By.CSS_SELECTOR, "#messages > :nth-child(1) > :nth-child(2)")
    PRODUCT_NAME_CONFIRM = (By.CSS_SELECTOR, "#messages > :nth-child(1) > :nth-child(2) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_BENEFIT = (By.CSS_SELECTOR, "#messages > :nth-child(2) > :nth-child(2)")
    PRODUCT_BENEFIT = (By.CSS_SELECTOR, "#messages > :nth-child(2) > :nth-child(2) strong")
    MESSAGE_PAYMENT = (By.CSS_SELECTOR, ".alert-info > :nth-child(2)")
    PRODUCT_PAYMENT_CONFIRM = (By.CSS_SELECTOR, ".alert-info > :nth-child(2) strong")
    PRODUCT_PAYMENT_BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_PAYMENT = (By.CSS_SELECTOR, ".product_main .price_color")

