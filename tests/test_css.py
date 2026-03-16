import time
from pages.box_page import TextBoxPage

def test_text_box_submit(browser):
    text_box = TextBoxPage(browser)

    text_box.visit()
    time.sleep(1)

    assert text_box.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')

    assert text_box.btn_submit.check_css('backgroundColor', 'rgba(10, 88, 202, 1)')
    assert text_box.btn_submit.check_css('borderColor', 'rgb(10, 83, 190)')