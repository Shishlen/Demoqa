import time
from pages.box_page import TextBoxPage

def test_clear_text(browser):
    box_page = TextBoxPage(browser)

    box_page.visit()
    box_page.full_name.send_keys("test_1")
    time.sleep(2)
    box_page.full_name.clear()
    time.sleep(2)

    assert box_page.full_name.get_text() == ""