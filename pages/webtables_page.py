from pages.base_page import BasePage
from Components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        # Кнопки
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_edit = WebElement(driver, '#edit-record-4')
        self.btn_delete = WebElement(driver, '#delete-record-4 > svg > path')

        # Поля ввода
        self.first_name_area = WebElement(driver, '#firstName')
        self.last_name_area = WebElement(driver, '#lastName')
        self.email_area = WebElement(driver, '#userEmail')
        self.age_area = WebElement(driver, '#age')
        self.salary_area = WebElement(driver, '#salary')
        self.department_area = WebElement(driver, '#department')

        # Локатор строк
        self.table = WebElement(driver, "#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7 > div.container-fluid > div.web-tables-wrapper > table > tbody")


