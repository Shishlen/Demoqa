from pages.base_page import BasePage

class ElementPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

    def get_center_text(self):
        return str(self.find_element('div.col-md-6').text)

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False