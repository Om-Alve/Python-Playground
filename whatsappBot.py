from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get('https://web.whatsapp.com')

# Wait for the page to load
time.sleep(15)

# Find the search box web element by class name
search_box = chrome.find_element(by=CLASS, value='_2vDPL')

# Enter the contact name and press enter
search_box.send_keys('You')
search_box.send_keys(Keys.ENTER)

while True:
    pass
