from selenium import webdriver
from PIL import Image
import time
import requests
import shutil
import os
import argparse

# Discussion with source: https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

# ChromeDriver download: https://sites.google.com/a/chromium.org/chromedriver/downloads
# ChromeDriver explanation: https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver

def save_img(inp,img,i, directory):
  try:
    filename = inp+str(i)+'.jpg'
    response = requests.get(img,stream=True)
    image_path = os.path.join(directory, filename)
    with open(image_path, 'wb') as file:
      shutil.copyfileobj(response.raw, file)
    print('Saved image:', filename)
  except Exception:
    pass

def find_urls(inp,url,driver, directory, num_images=10):
  driver.get(url)
  print('Scrolling for a bunch of images...')
  for _ in range(500):
    driver.execute_script("window.scrollBy(0,10000)")
    try:
      driver.find_element_by_css_selector('.mye4qd').click()
    except:
      continue
  print('Saving images..')
  for j, imgurl in enumerate(driver.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]')):
    try:
      if j >= num_images:
        return
      imgurl.click()
      img = driver.find_element_by_xpath('//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
      save_img(inp,img,j, directory)
      time.sleep(1.5)
    except:
      pass
            
if __name__ == "__main__":
  print('Starting scraper...')
  parser = argparse.ArgumentParser(description='Scrape Google images')
  parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
  parser.add_argument('-d', '--directory', default='../Downloads/', type=str, help='save directory')
  parser.add_argument('-n', '--num_images', default=10, type=int, help='number of images to save')
  args = parser.parse_args()
  driver = webdriver.Chrome('/home/minh/Downloads/chromedriver_linux64/chromedriver')
  directory = args.directory
  inp = args.search
  num_images = args.num_images
  if not os.path.isdir(directory):
    os.makedirs(directory)
  url = 'https://www.google.com/search?q='+str(inp)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'
  find_urls(inp,url,driver, directory, num_images)
  print('Finished scraping!')
