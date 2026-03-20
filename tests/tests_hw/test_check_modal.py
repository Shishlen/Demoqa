import pytest
from pages.modal_dialogs import ModalDialogs
import time

def test_modal_dialogs(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    if not modal_page.small_modal_btn.exist():
        pytest.skip('skiped')

    assert modal_page.small_modal_btn.exist()
    assert modal_page.large_modal_btn.exist()

    modal_page.small_modal_btn.click()
    time.sleep(1)
    modal_page.small_close_btn.click()
    assert not modal_page.modal_dialog.exist()


    modal_page.large_modal_btn.click()
    time.sleep(1)
    modal_page.large_close_btn.click()
    assert not modal_page.modal_dialog.exist()