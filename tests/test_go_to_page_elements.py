from pages.demoqa import DemoQa
from pages.elements_page import ElementPage
import time

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementPage(browser)


    demo_qa_page.visit()
    time.sleep(2)
    assert demo_qa_page.equal_url()
    demo_qa_page.click_on_the_btn()
    time.sleep(2)
    assert element_page.equal_url()