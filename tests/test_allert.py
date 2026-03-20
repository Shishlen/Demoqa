import time
from pages.alerts_page import AlertPage

def test_alert(browser):
    alert_page = AlertPage(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alert_button.click()
    time.sleep(2)
    assert alert_page.alert()

def test_alert_text(browser):
    alert_text = AlertPage(browser)

    alert_text.visit()
    alert_text.alert_button.click()
    assert alert_text.alert().text == "You clicked a button"

    alert_text.alert().accept()

    assert not alert_text.alert()

def test_confirm(browser):
    alert_confirm = AlertPage(browser)

    alert_confirm.visit()
    alert_confirm.confirm_button.click()
    time.sleep(2)
    alert_confirm.alert().dismiss()

    assert alert_confirm.confirm_result.get_text() == "You selected Cancel"

def test_alert_prompt(browser):
    alert_prompt = AlertPage(browser)
    text_1 = 'Nicole'

    alert_prompt.visit()
    alert_prompt.prompt_button.click()
    time.sleep(2)
    alert_prompt.alert().send_keys(text_1)
    alert_prompt.alert().accept()

    assert alert_prompt.prompt_result.get_text() == f'You entered {text_1}'
