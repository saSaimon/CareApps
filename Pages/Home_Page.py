from Pages.Base_Page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Home(Page):
    TOTAL_JOB_CART = (By.XPATH, "//div[normalize-space()='Total Job']")
    VIEWED_APPLICATION_CART = (By.XPATH, "//div[normalize-space()='Viewed Application']")
    UNSEEN_APPLICATION_CART = (By.XPATH, "//div[normalize-space()='Unseen Application']")
    TOTAL_JOB_APPLICATION_CART = (By.XPATH, "//div[@class='mb-4 font-bold text-black-500 text-18']")
    ACCEPTED_APPLICATION_CART = (By.XPATH, "//div[@class='font-medium text-18']")
    SUBMITTED_APPLICATION_CART = (By.XPATH, "//div[@class='flex-1 font-bold text-black text-20 whitespace-nowrap']")
    JOBS_CART = (By.XPATH, "//span[normalize-space()='View Jobs']")
    COMPLETION_RATIO = (By.XPATH, "//div[@class='font-bold text-white text-20']")
    JOB_APPLICATION_BUTTON = (By.XPATH, "//a[@href='/app/recruitment/candidate-list']//div[@class='mx-auto max-w-fit']//button[@type='button']")
    VIEW_JOBS_BUTTON = (By.CSS_SELECTOR, '[href="/app/recruitment/job-board"] div button ')
    JOB_BOARD_TEXT = (By.XPATH, "//div[@class='font-bold text-20']")


    def verify_total_job_present(self):
        self.find_element(*self.TOTAL_JOB_CART)

    def verify_viewed_application_present(self):
        self.find_element(*self.VIEWED_APPLICATION_CART)

    def verify_unseen_application_present(self):
        self.find_element(*self.UNSEEN_APPLICATION_CART)

    def verify_total_job_application_present(self):
        self.find_element(*self.TOTAL_JOB_APPLICATION_CART)

    def verify_accepted_application_present(self):
        self.find_element(*self.ACCEPTED_APPLICATION_CART)

    def verify_submitted_application_present(self):
        self.find_element(*self.SUBMITTED_APPLICATION_CART)

    def verify_jobs_cart_present(self):
        self.find_element(*self.JOBS_CART)

    def verify_completion_ratio_present(self):
        self.find_element(*self.COMPLETION_RATIO)

    def click_job_application_button(self):
        self.click(*self.JOB_APPLICATION_BUTTON)

    def click_view_jobs(self):
        self.click(*self.VIEW_JOBS_BUTTON)

    def verify_job_board_text(self, context):
        self.verify_text('Job Board', *self.JOB_BOARD_TEXT, context=context)

    def verify_candidate_list_text(self, context):
        self.verify_text('Candidates List', *self.JOB_BOARD_TEXT, context=context)

    def back_to_previous_page(self):
        sleep(5)
        self.back()




