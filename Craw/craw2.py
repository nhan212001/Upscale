from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import io
from PIL import Image
import time
import numpy as np

PATH = "C:\PBL\Craw\chromedriver.exe"

from selenium import webdriver

wd = webdriver.Chrome(PATH)
url = "https://www.pexels.com/search/animal/"
wd.get(url)

def scroll_down(wd, delay):
    script = "window.scrollTo(window.scrollY, document.body.scrollHeight - 1500);"
    wd.execute_script(script)
    time.sleep(delay)
 

def get_images_from_web(wd, delay, max_images):
    wait = WebDriverWait(wd, 5)
    image_urls = set()
    list_element = wd.find_elements(By.TAG_NAME, "img")

    while len(list_element) < max_images:
        scroll_down(wd, delay)
        new_list_element = wd.find_elements(By.TAG_NAME, "img")

        # if len(new_list_element) == len(list_element):
        #     ratio += 0.02

        # list_element = np.array(list_element)
        # new_list_element = np.array(new_list_element)
        # index = np.where(np.isin(new_list_element,list_element) == False)
        
        # for img in new_list_element[index]:
        #     try:
        #         if img.get_attribute('src') and 'http' in img.get_attribute('src'):
        #             image_urls.add(img.get_attribute('src'))
        #     except:
        #         continue

        list_element = new_list_element
        print(len(list_element))

    for img in list_element:
        try:
            if img.get_attribute('src') and 'http' in img.get_attribute('src'):
                image_urls.add(img.get_attribute('src'))
            print(len(image_urls))
        except:
            continue
    # i = 0
    # for img in list_element:
    #     i+=1
    #     print(i)
    #     if img.get_attribute('src') and 'http' in img.get_attribute('src'):
    #         image_urls.add(img.get_attribute('src'))
    # print(len(image_urls))
    return image_urls

def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		# print("Success")
	except Exception as e:
		print('FAILED -', e)


urls = get_images_from_web(wd, 1, 7000)
# print(urls)
i = 0
for url in urls:
    if i<=5000:
        download_image("C:\PBL\Craw\\train\ " , url,str(i) + ".jpg")
    else:
        download_image("C:\PBL\Craw\\test\ " , url,str(i) + ".jpg")
    i+=1
wd.quit()