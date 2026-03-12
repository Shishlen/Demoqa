from pages.base_page import BasePage
from Components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_modal = WebElement(driver, '.btn.btn-primary')
        self.go_to_main_page = WebElement(driver, '#root > header > a')
        self.elem_icon = WebElement(driver, '#root > header > a > img')

    def refresh(self):
        return self.driver.refresh()

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
