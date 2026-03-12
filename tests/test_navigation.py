from pages.demoqa import DemoQa
from pages.elements_page import ElementPage
import time

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementPage(browser)

    demo_qa_page.visit()
    time.sleep(2)
    demo_qa_page.btn_elements()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert element_page.equal_url()
