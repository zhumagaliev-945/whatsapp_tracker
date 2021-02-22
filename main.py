from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path='/home/zhumagaliev/PycharmProjects/whatsapp_tracker/chromedriver')
browser.maximize_window()
browser.get('https://google.com/')
wait = WebDriverWait(browser, 5)

search_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//body/div[1]/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]')))
search_bar.send_keys('whatsapp web')
enter_action = ActionChains(browser)

enter_action.send_keys(Keys.ENTER)
enter_action.perform()
web_link = wait.until(EC.presence_of_element_located((By.XPATH, '//body[1]/div[7]/div[2]/div[9]/div[2]/div[1]/div[2]'
                                     '/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]/span[1]')))
web_link.click()
