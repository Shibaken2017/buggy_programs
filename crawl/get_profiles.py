'''
指定したidのpロフィールをゲットするのだ
'''
import logging
import os
import sys
import traceback
sys.path.append(os.path.join(os.pardir,"../"))
sys.path.append(os.pardir)
from selenium import webdriver
from tmp_picks.utils.handling_tsv import load_id_files
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
IMPLICITLY_WAIT_TIME=60

BASE_URL="?"




class Profiler:
    def __init__(self):
      self.__driver=webdriver.Chrome()
      self.option=False
    def exe_multi_ids(self,ids_fname,output_fname,option=False):
      '''
      optionでfollow,floower枢も取る
      :param ids_fname:
      :param output_fname:
      :param option:
      :return:
      '''
      self.option=option
      ids=load_id_files(ids_fname)
      for id in ids:
        self.exe(id,output_fname)
        time.sleep(1.4)


    def exe(self,id,fname):
      self.fname=fname

      target_url=BASE_URL.format(id)
      self.__driver.get(target_url)
      time.sleep(1.7)
      con=self.__driver.find_elements_by_xpath(r'/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div[2]/div/div[5]')#.#click()
      if con:
        con[0].click()
      name=self.__driver.find_element_by_xpath(r'/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div[2]/div/div[1]/h1').text
      job_title=self.__driver.find_elements_by_xpath(r'/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div[2]/div/div[2]')
      if len(job_title)==1:
        job_title=job_title[0].text
      else:
        job_title=""


      profile=self.__driver.find_element_by_xpath(r'/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div[2]/div/div[4]').text
      print(profile)
      speciality_tag=self.__driver.find_elements_by_xpath\
        (r'/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div[1]')
      if speciality_tag:
        speciality=""
        tmp=speciality_tag[0].find_elements_by_class_name(r'picker-speciality')
        for ele in tmp:
          speciality+=ele.text+" "
        speciality=speciality.strip()
      else:
        speciality=""


      num_of_like=self.__driver.find_element_by_xpath(r'/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div[2]/span').text
      follower=self.__driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[3]/span[1]").text
      follow=self.__driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[1]").text



      self.write_tsv(name,job_title,speciality,num_of_like,profile,follow,follower)






    def write_tsv(self,name,job_title,speciality,num_of_like,profile,follow,follower):
      if not os.path.exists(self.fname):
        with open(self.fname, "a")as writer:
          if self.option==True:
            writer.write("名前\t肩書き\tジャンル\tLike数\tプロフィール\tfollow\tfollower\n")

            writer.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(name, job_title, speciality, num_of_like, profile,follow,follower))

          else:
            writer.write("名前\t肩書き\tジャンル\tLike数\tプロフィール\n")

            writer.write('{}\t{}\t{}\t{}\t{}\n'.format( name, job_title, speciality,num_of_like,profile))
      else:
        with open(self.fname, "a")as writer:
          if self.option==True:
            writer.write(
              '{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(name, job_title, speciality, num_of_like, profile, follow,
                                                    follower))


          else:

            writer.write('{}\t{}\t{}\t{}\t{}\n'.format( name, job_title, speciality,num_of_like,profile))


if __name__=="__main__":
  tmp=Profiler()#
  #tmp.exe(r'122407')
  tmp.exe_multi_ids("id.txt","profiles_cgecj.tsv",True)




