from Pages.Login_Page import LoginPage
from Pages.Home_Page import Home

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.home_page = Home(self.driver)