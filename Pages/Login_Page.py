from selenium.webdriver.common.by import By
from Pages.Base_Page import Page


class LoginPage(Page):
    EMAIL_FIELD = (By.XPATH, "//input[@id='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    REMEMBERME_BUTTON = (By.XPATH, "//input[@id='isRemembered']")
    FORGOT_PASS_LINK = (By.CSS_SELECTOR, '[href="/auth/forgot-password"]')
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGO = (By.XPATH, "//img[@alt='CareApps-logo']")
    NO_USER_FOUND_MODAL = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[2]")
    PASSWORD_INVALID = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[2]")

    def enter_to_website(self, url):
        self.open_url(url)

    def input_email(self, text):
        self.input_text(text, *self.EMAIL_FIELD)

    def input_password(self, text):
        self.input_text(text, *self.PASSWORD_FIELD)

    def click_remember_me_button(self):
        self.click(*self.REMEMBERME_BUTTON)

    def click_forgot_pass_link(self):
        self.click(*self.FORGOT_PASS_LINK)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)

    def is_logo_present(self):
        logo = self.find_element(*self.LOGO)
        assert logo, f'Logo is not found'

    def login_failed(self, context):
        self.verify_text('No such user found!!', *self.NO_USER_FOUND_MODAL, context=context)

    def password_invalid(self,context):
        self.verify_text('User password is not valid', *self.PASSWORD_INVALID, context=context)
