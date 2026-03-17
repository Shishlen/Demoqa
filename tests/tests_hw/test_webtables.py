import time
from pages.webtables_page import WebTables

def test_webtables_form(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    time.sleep(1)

    web_tables.btn_add.click()


    web_tables.btn_submit.click()

    assert web_tables.btn_submit.exist()
    time.sleep(1)


    web_tables.first_name_area.send_keys('Alex')
    web_tables.last_name_area.send_keys('Saint')
    web_tables.email_area.send_keys('a.saint@gmoil.nope')
    web_tables.age_area.send_keys('25')
    web_tables.salary_area.send_keys('145000')
    web_tables.department_area.send_keys('IT')
    time.sleep(1)

    web_tables.btn_submit.click()

    assert 'Alex' in web_tables.table.get_text()
    assert 'Saint' in web_tables.table.get_text()
    assert 'a.saint@gmoil.nope' in web_tables.table.get_text()
    time.sleep(1)

    web_tables.btn_edit.click() # Здесь падает
    web_tables.first_name_area.send_keys('CTRL' + 'a', 'Will')
    assert 'Will' in web_tables.table.get_text()
    time.sleep(1)

    web_tables.btn_submit.click()
    assert 'Alex' in web_tables.table.get_text()
    time.sleep(1)

    web_tables.btn_delete.click() # Здесь упадет
    assert not 'Will' in web_tables.table.get_text()
    assert not 'Saint' in web_tables.table.get_text()
    assert not 'a.saint@gmoil.nope' in web_tables.table.get_text()



