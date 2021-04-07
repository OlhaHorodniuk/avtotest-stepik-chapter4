from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    # LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    # LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_submit")

    # REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    # REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    # REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    # REGISTER_BUTTON = (By.CSS_SELECTOR, "#registration_submit")


class ProductPageLocators:
    NAME_PRODUCT = (By.XPATH, "//div[contains(@class, 'col-sm-6 product_main')]/h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")

    # button
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[class $="btn-add-to-basket"]')

    # alert
    ALERT_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ALERT_PRICE_PRODUCT = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BUTTON_VIEW_BASKET = (By.XPATH, '//a[contains(@href, "basket")]')


class BasketPageLocators:
    TABLE_PRODUCT = (By.CLASS_NAME, 'basket-items')
    MESSAGE_ABOUT_EMPTY_BASKET = (By.XPATH, '//*[@id="content_inner"]/p')

