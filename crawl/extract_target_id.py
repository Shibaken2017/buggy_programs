'''
news picksからターゲットのidget!"
'''
import bs4


with open("ex.html","r")as reader:
  contents=reader.read()

example_soup=bs4.BeautifulSoup(contents)

elements=example_soup.find_all(class_=r'recommended-category follow-btn-wrapper')
for ele in elements:
  if ele.get("data-theme-id") =="8"or ele.get("data-theme-id") =="26":
    cards=ele.find_all(class_=r'recommended-picker-card')
    for card in cards:
      with open("id.txt","a")as writer:
        id=card.select("a")[0].get(r'data-user')
        name=card.find(class_="user-name _ellipsised").string
        writer.write(id+"\t"+name+"\n")

