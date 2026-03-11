from pages.accordian import Accordian
import time

def test_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    time.sleep(2)

    assert accordian_page.section_1_content.visible()

    accordian_page.section_1_heading.click()
    time.sleep(2)

    assert not accordian_page.section_1_content.visible()

def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    time.sleep(2)

    assert not accordian_page.section_2_content.visible()
    assert not accordian_page.section_2_content.visible()
    assert not accordian_page.section_3_content.visible()