from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("-headless")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://statsroyale.com/tr/profile/2L299CRPP")
button = driver.find_element_by_xpath('//*[@id="refresh-profile"]')
button.click()
driver.quit()