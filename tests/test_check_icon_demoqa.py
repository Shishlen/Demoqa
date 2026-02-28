# from selenium import webdriver # вынесено в общий файл
from selenium.webdriver.common.by import By

def test_check_icon_demoqa(browser):
    # driver = webdriver.Chrome() # вынесено в общий файл
    browser.get('https://demoqa.com/')

    icon = browser.find_elements(By.CSS_SELECTOR, '#app > header > a')

    if icon is None:
        print('No icon found')
    else:
        print('Icon found')