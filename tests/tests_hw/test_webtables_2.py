import time
from pages.webtables_page import WebTables

def test_pagination(browser):
    web_tables = WebTables(browser)
    web_tables.visit()

    # Предусловия
    for i in range(3):
        web_tables.btn_add.click()
        web_tables.first_name.send_keys(f'Alex{i}')
        web_tables.last_name.send_keys(f'Saint{i}')
        web_tables.email.send_keys(f'a.saint{i}@example.com')
        web_tables.age.send_keys('25')
        web_tables.salary.send_keys('145000')
        web_tables.department.send_keys('IT')
        web_tables.btn_submit.click()


    assert web_tables.btn_next.get_dom_attribute('disabled') is not None
    assert web_tables.btn_previous.get_dom_attribute('disabled') is not None

    for i in range(5):
            web_tables.btn_add.click()
            web_tables.first_name.send_keys(f'AlexB{i}')
            web_tables.last_name.send_keys(f'SaintB{i}')
            web_tables.email.send_keys(f'a.saintB{i}@example.com')
            web_tables.age.send_keys('25')
            web_tables.salary.send_keys('145000')
            web_tables.department.send_keys('IT')
            web_tables.btn_submit.click()

    web_tables.btn_next.scroll_to_element()
    time.sleep(1)
    web_tables.btn_next.click()
    time.sleep(2)
    assert "2 of 2" in web_tables.page_info.get_text()

    web_tables.btn_previous.click()
    time.sleep(2)
    assert "1 of 2" in web_tables.page_info.get_text()


