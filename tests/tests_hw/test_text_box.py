import time
from pages.box_page import TextBoxPage

def test_text_box(browser):
    text_1 = ' Tester Testovich 123'
    text_2 = ' Moscow'
    box_page = TextBoxPage(browser)


    box_page.visit()
    time.sleep(2)
    box_page.full_name.send_keys(text_1)
    box_page.current_address.send_keys(text_2)

    box_page.btn_submit.click()
    time.sleep(2)

    assert text_1 in box_page.result_name.get_text()
    assert text_2 in box_page.result_address.get_text()