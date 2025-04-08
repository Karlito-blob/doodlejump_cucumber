from selenium.webdriver import Chrome

class CommonPage:

    def __init__(self, browser: Chrome):
        self.browser = browser