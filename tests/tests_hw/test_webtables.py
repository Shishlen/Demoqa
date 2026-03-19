import time
from pages.webtables_page import WebTables

def test_webtables_form(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.btn_add.click()

    assert web_tables.btn_submit.exist()

    web_tables.first_name.send_keys('Alex')
    web_tables.last_name.send_keys('Saint')
    web_tables.email.send_keys('a.saint@example.com')
    web_tables.age.send_keys('25')
    web_tables.salary.send_keys('145000')
    web_tables.department.send_keys('IT')
    web_tables.btn_submit.click()
    time.sleep(1)

    assert not web_tables.modal_dialog.exist()
    assert 'Alex' in web_tables.table_first_name.get_text()
    assert 'a.saint@example.com' in web_tables.table_first_name.get_text()

    time.sleep(1)
    web_tables.btn_edit.click()
    assert web_tables.modal_registration.exist()
    time.sleep(1)

    web_tables.first_name.clear()
    web_tables.first_name.send_keys('William')
    web_tables.btn_submit.click()
    assert 'William' in web_tables.table_first_name.get_text()
    assert 'a.saint@example.com' in web_tables.table_first_name.get_text()
    time.sleep(1)

    web_tables.btn_delete.click()

    time.sleep(1)
    elements = browser.find_elements("xpath", "//div[text()='William']")
    assert len(elements) == 0

