from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
import time

driver = webdriver.Chrome()
driver.get('https://finance.yahoo.com/gainers')


chance = driver.find_element_by_xpath(
    '//*[@id="scr-res-table"]/div[1]/table/thead/tr/th[4]')
actions = ActionChains(driver)
#stockname = driver.find_element_by_id('')

for i in range(2):
    actions.move_to_element(chance)
    actions.click(chance)


elem = driver.find_element_by_id('quote-header-info')
price = elem.find_elements_by_tag_name('span')[3]
print(price.txt)

actions.perform()
