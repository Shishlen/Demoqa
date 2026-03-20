import time
from pages.alerts_page import AlertPage

def test_alert(browser):
    alert_page = AlertPage(browser)

    alert_page.visit()
    time.sleep(2)
    assert alert_page.timer_button.exist()
    alert_page.timer_button.click()
    time.sleep(6)
    assert alert_page.alert().text == "This alert appeared after 5 seconds"