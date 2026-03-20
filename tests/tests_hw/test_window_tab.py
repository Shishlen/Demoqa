import time
from pages.window_tab import WindowTab

def test_window_tab(browser):
    window_tab = WindowTab(browser)
    window_tab.visit()
    time.sleep(1)

    assert window_tab.home_button.get_text() == "Home"
    assert window_tab.home_button.get_dom_attribute('href') == "https://demoqa.com/"

    window_tab.home_button.click()
    time.sleep(1)
    assert len(browser.window_handles) == 2