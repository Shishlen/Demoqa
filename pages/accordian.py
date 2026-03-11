from pages.base_page import BasePage
from Components.components import WebElement

class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_1_content = WebElement(driver, '#accordianContainer > div > div:nth-child(1) > div > div > p')
        self.section_1_heading = WebElement(driver, '#accordianContainer > div > div:nth-child(1) > h2 > button')
        self.section_2_content = WebElement(driver, '#accordianContainer > div > div:nth-child(2) > div > div > p:nth-child(1)')
        self.section_2_content = WebElement(driver, '#accordianContainer > div > div:nth-child(2) > div > div > p:nth-child(2)')
        self.section_3_content = WebElement(driver, '#accordianContainer > div > div:nth-child(3) > div > div > p')