import time

from selenium.webdriver.common.keys import Keys

from pages.form_page import FormPage

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testerov")
    form_page.user_email.send_keys("tester@tester.ru")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("1111111111")
    form_page.btn_hobbies_3.click_force()
    form_page.current_address.send_keys("Russia, Moscow, Kuznetsovskaya, 14")
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.modal_dialog_close.click()

def test_insert_values(browser):
    text_1 = "NCR"
    text_2 = "Noida"

    form_page = FormPage(browser)

    form_page.visit()
    form_page.btn_state.click()
    form_page.btn_state.send_keys(text_1)
    time.sleep(1)
    form_page.btn_state.send_keys(Keys.ENTER)
    form_page.btn_city.click()
    form_page.btn_city.send_keys(text_2)
    time.sleep(1)
    form_page.btn_city.send_keys(Keys.ENTER)