import time
from pages.webtables_page import WebTables

def test_sort_webtables(browser):
    webtable_sorted = WebTables(browser)
    webtable_sorted.visit()
    time.sleep(1)

    headers = webtable_sorted.headers.find_elements()

    for header in headers:
        sort_before = header.get_dom_attribute("class")
        try:
            header.click()
        except:
            continue

        sort_after = header.get_dom_attribute("class")
        assert not sort_before == sort_after