
import logging
import os
import sys
import traceback
sys.path.append(os.path.join(os.pardir,"../"))
sys.path.append(os.pardir)
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.keys import Keys
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from utils.file_check import check_ts_csv
from utils.send_message_to_slack import send_image_to_slack,send_text_to_slack
from utils.spread_helper import    write_spread_sheet,DOC_ID
from selenium.webdriver.common.action_chains import ActionChains
IMPLICITLY_WAIT_TIME=120
logging.basicConfig(filename="ui_checker.log",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')





def get_page_source(target_url):
  driver = webdriver.Chrome()
  driver.implicitly_wait(IMPLICITLY_WAIT_TIME)
  driver.get(target_url)
  time.sleep(5)
  with open("ex.html","w")as writer:
    writer.write(driver.page_source)
  driver.quit()



if __name__=="__main__":

  get_page_source(r'recommended')


