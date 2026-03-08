# Создайте директорию tests_hw в папке tests все домашние тесты создавайте в ней
# 1. в классе компонентов создайте метод для получения текста с элементов get_text(self).
#  текст из элемента считывайте так str(self.find_element().text)
# 2. в файле test_check_text.py реализуйте таст кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
# 3. в файле test_check_text.py реализуйте таст кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. через кнопку перейти на страницу 'https://demoqa.com/elements'
# c. проверить что текст по центру == 'Please select an item from left to start practice.'


from pages.demoqa import DemoQa
import time

from pages.elements_page import ElementPage


def test_check_text_footer(browser):

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    time.sleep(2)

    footer_text = demo_qa_page.get_text('footer span')

    assert footer_text == '© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_center_pos(browser):

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    time.sleep(1)

    demo_qa_page.click_on_the_btn()

    element_page = ElementPage(browser)
    text_pos_center = element_page.get_center_text()

    assert text_pos_center == "Please select an item from left to start practice."
