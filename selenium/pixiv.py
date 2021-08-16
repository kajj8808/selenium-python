from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import urllib.request
import csv

def save_to_csv_file( items , name = "0"):
    file = open(f"{name}.csv", mode="w", encoding="utf-8", newline='')
    writer = csv.writer(file)
    writer.writerow(["title", "href", "picture" , "user_name" , "user_href" , "user_image"])
    for item in items:
        writer.writerow([item["title"] ,item["href"] ,item["picture"] ,item["user_name"] ,item["user_href"] ,item["user_image"]])
    return

def pixiv_login():
  with open('pixiv_login_config.json' , 'r') as fill:
    login_data = json.load(fill)
  #pixiv intial page login btn
  driver.find_element_by_class_name("signup-form__submit--login").click()
  driver.implicitly_wait(time_to_wait = 5)
  input_container = driver.find_elements_by_css_selector("#LoginComponent > form > div.input-field-group > div")
  #id input  
  input_container[0].find_element_by_tag_name("input").send_keys(login_data['ID'])
  #password input
  input_container[1].find_element_by_tag_name("input").send_keys(login_data['PASSWORD'])
  driver.find_element_by_css_selector("#LoginComponent > form > button").click()
  #다음에하기
  driver.find_elements_by_css_selector(".acb5nq-0.dDjvY.sc-1fnsiiu-2.dBbGNv")[1].click()
  driver.implicitly_wait(time_to_wait = 5)
  return 

def export_pixiv_data():
  items = []
  recommend_list = driver.find_elements_by_css_selector(".sc-9y4be5-0.CMuIj > ul > li")
  for index in range(2 , len(recommend_list) - 2):
    #get pixiv site  
    try:                                     
        ul = "/html/body/div[1]/div[2]/div[2]/div[5]/div/section/div[2]/div/div/ul"
        title_item = driver.find_element_by_xpath(f"{ul}/li[{index}]/div/div[2]/a")
        user_item = driver.find_element_by_xpath(f"{ul}/li[{index}]/div/div[3]/div/a")
        user_profile = driver.find_element_by_xpath(f"{ul}/li[{index}]/div/div[3]/div/div/a/div/img") # 수정 이거는 사진찍기 방식으로!
        image = driver.find_element_by_xpath(f"{ul}/li[{index}]/div/div[1]/div/a/div[2]/img")
        
        title = title_item.text
        href = title_item.get_attribute("href")
        picture = image.get_attribute("src") # 수정 이거는 사진찍기 방식으로!
        user_name = user_item.text
        user_href = user_item.get_attribute("href")
        user_image = user_profile.get_attribute("src")

        items.append({
          "title" : title,
          "href" : href,
          "picture" : picture,
          "user_name" : user_name,
          "user_href" : user_href,
          "user_image" : user_image,
        })
    except :
        continue
    save_to_csv_file(items)
  return 0
  
driver = webdriver.Firefox()
driver.get("https://www.pixiv.net/")
pixiv_login()
export_pixiv_data()
""" 
elem = driver.find_element_by_name("q")
elem.send_keys("jocoding")
elem.send_keys(Keys.RETURN) 
driver.implicitly_wait(time_to_wait = 5)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click() 
time.sleep(1)
image_url = driver.find_element_by_css_selector('.n3VNCb').get_attribute("src")
urllib.request.urlretrieve(image_url , "jo.jpg") """
""" assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()

elem.send_keys(Keys.RETURN) 
assert "No results found." not in driver.page_source
driver.close() """