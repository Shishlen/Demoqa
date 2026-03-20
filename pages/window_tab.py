from Components.components import WebElement
from pages.base_page import BasePage

class WindowTab(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)

        self.home_button = WebElement(driver, '#simpleLink')