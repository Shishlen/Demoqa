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
    alert_confirm.confirm_button.dismiss()

    assert alert_confirm.alert().text == "You selected Cancel"

