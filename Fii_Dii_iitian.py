from selenium import webdriver
import numpy as np
import schedule
import telegram
from datetime import datetime
import time
from pytz import timezone
from selenium.webdriver.chrome.options import Options
import os
import pyscreenshot as ImageGrab

# python3 -m pip install Pillow pyscreenshot

now = datetime.now()
format = "%Y-%m-%d %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
ocTime = now_asia.strftime(format)
strTime = str(ocTime).split(" ")
reqTime = strTime[0]+"_"+strTime[1]
url = 'https://iitiantrader.in/market-data/'
b_token = '5817461626:AAHp1IIIMkQGWFTqIuu84lYOoxlO8KS7CZo'
channel_id = '@swingTradeScreenedStocks'


def get_fiiDii_market_data(url):
    path = os.path
    imgName = f"screnshot-{reqTime}"
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(
        options=options, executable_path='/usr/lib/chromium-browser/chromedriver')
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    closeIcon = driver.find_element("xpath", "//i[@class='eicon-close']")
    closeIcon.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(3)
    screenshot = ImageGrab.grab()
    filePath = f".screenshots/{imgName}"
    screenshot.save(filePath)
    print("Taken screenshot successfully")


get_fiiDii_market_data(url)
