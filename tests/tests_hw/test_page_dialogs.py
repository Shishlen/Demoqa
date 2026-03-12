from pages.modal_dialogs import ModalDialogs
import time

def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    time.sleep(2)

    assert modal_elements.btns_modal.check_count_elements(count=5)
    # тест будет провален, поскольку на странице две кнопки

def test_navigation_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()
    time.sleep(2)
    modal_page.refresh()
    modal_page.go_to_main_page.click()
    time.sleep(1)
    browser.set_window_size(900, 400)
    time.sleep(2)
    modal_page.forward()

    assert modal_page.get_url() == 'https://demoqa.com/'
    assert modal_page.get_title() == 'demosite'

    browser.set_window_size(1000, 1000)
    time.sleep(2)