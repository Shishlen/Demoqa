import time
from pages.box_page import TextBoxPage

def test_placeholder(browser):
    box_page = TextBoxPage(browser)

    box_page.visit()
    time.sleep(2)
    assert box_page.full_name.get_attribute("placeholder") == 'Full Name'