#%%
# from https://www.youtube.com/watch?v=cddyhdb1GDw
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
import time
import os


#%%
path=r'C:\Users\peter\Documents\SeleniumTest'

#Use Incognito mode when scraping

chrome_options = Options()
chrome_options.add_argument(" — incognito")
browser = webdriver.Chrome(options=chrome_options)
url = r'https://gmail.com/'
urls=browser.get(url)
# pages=int(input('How Many Pages Do You Want to Scrape? '))

# input email
emailInput = browser.find_element_by_xpath("//*[@id='identifierId']").send_keys("test1988mctest@gmail.com")

# click next buttom
nextButton = browser.find_element_by_xpath("//*[@id='identifierNext']").click()
type(nextButton)



browser.implicitly_wait(4)

# input password
#passWord = os.environ.get("gmailPassWord")
passWord = os.environ.get("gmailTestPassword") # testfgmail 
#passwordInput  = browser.find_element_by_xpath("//*[@id='password']").send_keys(passWord)
#passwordInput  = browser.find_element_by_xpath("//*[@id='password']").send_keys(passWord)
 
passwordInput  = browser.find_element_by_name('password').send_keys(passWord)

passNextButton = browser.find_elements_by_xpath("//*[@id='passwordNext']/span/span")[0].click()

sent  = browser.find_elements_by_xpath("//*[@id=':3z']")[0].click()
browser.implicitly_wait(5)

email = browser.find_elements_by_xpath("//*[@id=':1']/div/div[2]/div[3]/div[3]/table")[0].click()
# %%
