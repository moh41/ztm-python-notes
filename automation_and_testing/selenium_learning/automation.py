import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")

browser.maximize_window()
browser.get("https://duckduckgo.com")

print("DuckDuckGo" in browser.title)
searchbox = browser.find_element_by_id("search_form_input_homepage")
searchbox.send_keys("Zero to Mastery")
searchbutton = browser.find_element_by_id("search_button_homepage")
searchbutton.click()
time.sleep(3)

browser.quit()