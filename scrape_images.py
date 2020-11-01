from selenium import webdriver
from PIL import Image
import time
import os
import argparse
import re
import urllib.request
import socket
import tempfile

# Discussion with source: https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

# ChromeDriver download: https://sites.google.com/a/chromium.org/chromedriver/downloads
# ChromeDriver explanation: https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver

def save_img(inp,img,i, directory, tmp_dir_name):
  socket.setdefaulttimeout(5)

  try:
    tmp_filename = re.sub(r"\s+", '_', inp)+str(i)+'.jpg'
    tmp_filepath = os.path.join(tmp_dir_name, tmp_filename)
    urllib.request.urlretrieve(img, tmp_filepath)

    img = Image.open(tmp_filepath)

    # Write to output png
    filename = re.sub(r"\s+", '_', inp)+str(i)+'.png'
    img.save(os.path.join(directory, filename))
    print('Saved image:', filename)
  except Exception as e:
    print(e)
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
  with tempfile.TemporaryDirectory() as tmp_dir_name:
    print('Saving images..')
    for j, imgurl in enumerate(driver.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]')):
      print('{}-th image'.format(j))
      try:
        if j >= num_images:
          return
        print('clicking')
        imgurl.click()
        print('finding element')
        img = driver.find_element_by_xpath('//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        print('saving image')
        save_img(inp,img,j, directory, tmp_dir_name)
        time.sleep(1.5)
      except:
        pass


if __name__ == "__main__":
  print('Starting scraper...')
  parser = argparse.ArgumentParser(description='Scrape Google images')
  parser.add_argument('-s', '--search', default='california+house+fire', type=str, help='search term')
  parser.add_argument('-d', '--directory', default='../', type=str, help='save directory')
  parser.add_argument('-n', '--num_images', default=200, type=int, help='number of images to save')
  args = parser.parse_args()
  driver = webdriver.Chrome('../chromedriver')
  directory = args.directory
  inp = args.search
  num_images = args.num_images
  if not os.path.isdir(directory):
    os.makedirs(directory)
  if 'fire' in inp:
    url = 'https://www.google.com/search?q='+str(inp)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947&tbs=ic:specific%2Cisc:orange%2Cisz:l'
  else:
    url = 'https://www.google.com/search?q='+str(inp)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947&tbs=isz:l'
  find_urls(inp,url,driver, directory, num_images)
  print('Finished scraping!')
