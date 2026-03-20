from pages.base_page import BasePage
from Components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        # Кнопки
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_edit = WebElement(driver, 'edit-record-4', 'id')
        self.btn_delete = WebElement(driver, '//*[@id="delete-record-4"]', 'xpath')
        self.btn_next = WebElement(driver, "//button[text()='Next']", 'xpath')
        self.btn_previous = WebElement(driver, "//button[text()='Previous']", 'xpath')
        self.page_info = WebElement(driver, "//span[@class='-totalPages']")

        # Поля ввода
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        # Окна
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.modal_registration = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.table_first_name = WebElement(driver, '#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7 >'
                                                   ' div.container-fluid > div.web-tables-wrapper > table > '
                                                   'tbody > tr:nth-child(4)')
        self.page_info = WebElement(driver, "//div[contains(text(),'Page')]/strong", "xpath")

        self.headers = WebElement(driver, '.rt-th')