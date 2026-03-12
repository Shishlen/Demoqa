from pages.demoqa import DemoQa
import time

def test_seo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    time.sleep(2)
    assert browser.title == 'demosite'