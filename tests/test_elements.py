from pages.elements_page import ElementPage

def test_find_elements(browser):
    elements_page = ElementPage(browser)
    elements_page.visit()

    assert elements_page.btns_first_menu.check_count_elements(count=9)