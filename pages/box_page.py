from Components.components import WebElement
from pages.base_page import BasePage

class TextBoxPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.email = WebElement(driver, '#userEmail')
        self.current_address = WebElement(driver, '#currentAddress')
        self.permanent_address = WebElement(driver, '#permanentAddress')

        # Результирующие поля
        self.result_name = WebElement(driver, '#output #name')
        self.result_address = WebElement(driver, '#output #currentAddress')
        self.btn_submit = WebElement(driver, '#submit')