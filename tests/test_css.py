import time
from pages.box_page import TextBoxPage

def test_text_box_submit(browser):
    text_box = TextBoxPage(browser)

    text_box.visit()
    time.sleep(1)

    assert text_box.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')

    assert text_box.btn_submit.check_css('background-color', 'rgba(13, 110, 253, 1)')
    assert text_box.btn_submit.check_css('border-color', 'rgb(13, 110, 253)')