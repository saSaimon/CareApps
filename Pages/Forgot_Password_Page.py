from Pages.Base_Page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ForgotPasswordPage(Page):
    EMAIL_BOX = (By.XPATH, "//input[@id='email']")
    SEND_NOW_BUTTON = (By.XPATH, "//button[@type='submit']")
    SIGN_IN_BUTTON = (By.XPATH, '//a[@href="/auth/login"]')
    TEXT = (By.CSS_SELECTOR, '[class="mt-4 font-normal text-md sm:text-xl text-black-400"]')
    EMAIL_NOT_VALID_TEXT = (By.CSS_SELECTOR, '[class="right-0 bottom-50 flex items-start text-red"] p')

    def type_email_to_email_address(self, email):
        self.input_text(email, *self.EMAIL_BOX)

    def click_send_now_button(self):
        self.click(*self.SEND_NOW_BUTTON)

    def verify_text_email_sent(self, context):
        self.verify_text('A reset link has been sent to the registered mail! Please check your mail including junk folder.', *self.TEXT, context=context)

    def verify_email_not_valid_text(self, context):
        self.verify_text('Email is not valid', *self.EMAIL_NOT_VALID_TEXT, context=context)