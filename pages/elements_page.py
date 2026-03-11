from Components.components import WebElement
from pages.base_page import BasePage

class ElementPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_elements = WebElement(driver, 'div.col-12:nth-child(2)')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, '#item-0 > a > span')
        self.btn_sidebar_first_checkbox = WebElement(driver, '#item-1 > a > span')

    def get_center_text(self):
        return str(self.find_element('div.col-md-6').text)

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False