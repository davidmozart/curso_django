from pathlib import Path
from selenium import webdriver
from time import sleep
from selenium import webdriver
import os



ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' /CHROMEDRIVER_NAME

# print(ROOT_PATH)

# print(CHROMEDRIVER_PATH)
# '--headless' serve para não executar o navegador
def make_chrome_browser():
    browser = webdriver.Chrome()
    return browser


if __name__ == '__main__':
    browser = make_chrome_browser('--headless')
    browser.get('http://udemy.com/')
    sleep(5)
    browser.quit()
