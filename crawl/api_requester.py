'''
news picksのAPIにリクエストする
'''
from retry import retry
import requests
import bs4
import os
import sys
sys.path.append(os.path.join(os.pardir,"../"))
sys.path.append(os.pardir)
import time
import logging
from tmp_picks.utils.handling_tsv import write_tsv,load_id_files
import datetime
logging.basicConfig(filename="api_requester.log",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import traceback
BASE_UIChecker = os.path.dirname(os.path.abspath(__file__))


PROXIES = {
  'http': 'http://proxy.service.datasection.com:9080',
  'https': 'proxy.service.datasection.com:9080',
}

class requester:
  def __init__(self):
    self.__save_dir="data_tmp"

  def __create_dir(self):
    '''
    cereate dir for screenshots
    :return:
    '''
    self.__now_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    if not os.path.exists(os.path.join(BASE_UIChecker, "tsv_files")):
      os.makedirs(os.path.join(BASE_UIChecker, "screenshots"))

    self.__save_dir = os.path.join(BASE_UIChecker, "tsv_files", self.__now_str)
    os.makedirs(self.__save_dir)


  def exe_multi_ids(self,fname):
    self.__create_dir()
    ids=load_id_files(fname)
    for id in ids:
      try:
        self.exe(id)
      except Exception as err:
        print(traceback.format_exc())
        logging.error(traceback.format_exc())

  def exe(self,id):
    self.id=id
    logging.info("id={}".format(self.id))
    print(self.id)
    self.start_url="https://newspicks.com/user/{}/followers?".format(self.id)
    self.mode="follower"
    print(self.mode)
    logging.info(self.mode)
    elements = self.get_elements(self.start_url)
    while len(elements) > 0:
     elements = self.extract_info_from_elements(elements)




    self.start_url = "https://newspicks.com/user/{}/followings?".format(self.id)
    self.mode = "follow"
    logging.info(self.mode)
    print(self.mode)
    elements = self.get_elements(self.start_url)
    while len(elements) > 0:
      elements = self.extract_info_from_elements(elements)


  @retry(tries=5,delay=2)
  def get_elements(self,url):
    '''
      指定urlかｒatagのリストを返す
      :param url:
      :return:
      '''
    content = (requests.get(url, proxies=PROXIES).text)

    soup = bs4.BeautifulSoup(content)

    elements = soup.select("a")
    return elements

  def extract_info_from_elements(self,elements):
    for ele in elements:
      self.extract_info(ele)
    # 次のページのfromの値z
    next_from = elements[-1].get("data-key")

    new_url = self.start_url + "from=" + str(next_from)
    time.sleep(1.5)

    return self.get_elements(new_url)



  def extract_info(self,element):
    id=element.get("data-key")
    tmp_name = element.find(class_="username")
    if tmp_name:
      name=tmp_name.string
    else:
      name=""
    relation = element.find_all(class_="relation")
    follow = relation[0].find(class_="v").string
    follower = relation[1].find(class_="v").string
    title = ""
    titles_tag = element.find_all(class_="title")
    for ele in titles_tag:
      if ele.string:
        title += ele.string.strip() + " "
    title = title.strip()
    fname=os.path.join(self.__save_dir,self.id+".tsv")
    write_tsv(fname, id,name, title, follow, follower,self.mode)






if __name__=="__main__":
#https://newspicks.com/user/277827?t=followers
  tmp=requester()
  dir
tmp.exe_multi_ids("id.txt")
 # tmp.exe("541744")
  #tmp.exe("1047953")
#')
