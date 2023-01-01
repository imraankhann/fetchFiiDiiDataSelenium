from selenium import webdriver
import numpy as np
import schedule
import telegram
from datetime import datetime
import time
from pytz import timezone
from selenium.webdriver.chrome.options import Options
import os
import pyautogui
import requests

# python3 -m pip install Pillow pyscreenshot
# sudo apt-get install scrot

now = datetime.now()
format = "%Y-%m-%d %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
ocTime = now_asia.strftime(format)
splitTime = ocTime[11:16]
print(splitTime)
strTime = str(ocTime).split(" ")
reqTime = strTime[0]
intTime = int(splitTime[0:2])

url = 'https://iitiantrader.in/market-data/'
b_token = '5817461626:AAHp1IIIMkQGWFTqIuu84lYOoxlO8KS7CZo'
channel_id = '@swingTradeScreenedStocks'
imgName = f"screenshot-{reqTime}"


def get_fiiDii_market_data(url):
    if intTime > 21:
        path = os.getcwd()
        dirname = os.path.dirname(path)
        strPath = str(dirname)
        # absPath = strPath+"FII-DII-IITIAN/screenshots/"
        # print("Abs path : " + absPath)

        options = Options()
        options.headless = False
        driver = webdriver.Chrome(
            options=options, executable_path='/usr/lib/chromium-browser/chromedriver')
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        closeIcon = driver.find_element("xpath", "//i[@class='eicon-close']")
        closeIcon.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 220)")
        time.sleep(3)
        screenshot = pyautogui.screenshot()
        screenshot.save(imgName+".png")
        print("Taken screenshot successfully")
        bot = telegram.Bot(token=b_token)
        # file = {'photo': open(imgName+'.png', 'rb')}
        # bot.send_photo(chat_id=channel_id, files=file)
        method = "sendPhoto"
        params = {'chat_id': channel_id}
        files = {'photo': open(imgName+'.png', 'rb')}
        resp = requests.post(
            'https://api.telegram.org/botb_token/' + method, params, files=files)
        # /home/imran/Documents/Workspaces/FII-DII-IITIAN/screenshots
        print(resp.status_code)
    else:
        print("Not yet 9 PM")


if intTime > 23:
    os.remove(imgName+".png")


get_fiiDii_market_data(url)
