import datetime
import math
import os.path
import random
import re
import sys
import time
import pickle
import undetected_chromedriver as uc
from fake_useragent import UserAgent
ua = UserAgent()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import hashlib
from db_config import DbConfig
obj = DbConfig()

def create_md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

def page_write(pagesave_dir, file_name, data):
    if not os.path.exists(pagesave_dir):
        os.makedirs(pagesave_dir)
    file = open(file_name, "w", encoding='utf8')
    file.write(data)
    file.close()
    return "Page written successfully"

try:
    start = sys.argv[1]
    end = sys.argv[2]
except:
    start = 1
    end = 20000


qr = f"select * from {obj.product_links_table} where status='Done' and status_400001='pending' and id>{start} and id<{end} "
obj.cur.execute(qr)
results = obj.cur.fetchall()

for r in results:
    meesho_pid = r['meesho_pid']
    pin_code = '400001'
    id = r['id']

    url = f'https://www.meesho.com/s/p/{meesho_pid}'

    hashid = create_md5_hash(f'{url}_{pin_code}')

    # Set up undetected Chrome options
    options = uc.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode (optional)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"user-agent={ua.random}")

    driver = uc.Chrome(options=options)
    # Navigate to the website
    try:
        driver.get(url)
        # Load cookies from the file
        with open("cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        # Refresh the page to reflect the loaded cookies
        driver.refresh()
        # Optional: Wait for a while to see the result
        time.sleep(3)
        try:
            wait = WebDriverWait(driver, 20)
            input_pin = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="pin"]')))
            input_pin.click()

            input_pin.send_keys(pin_code) #entering zipcode
            check_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='pin']/following-sibling::button")))
            check_button.click()
            time.sleep(2)
            pincode_flag = True
        except Exception as e:
            print(e)
            pincode_flag = False
        data = driver.page_source


        try:
            data2 = re.findall('{"props":.*?</script>', data)[0]
            data2 = data2.replace('</script>', '')
        except:
            data2 = data

        today_date = datetime.datetime.today().strftime("%d_%m_%Y")

        pagesave_dir = rf"C:/Users/Actowiz/Desktop/pagesave/meesho/{today_date}"
        file_name = fr"{pagesave_dir}/{hashid}.html"
        page_write(pagesave_dir, file_name, data2)


        item = {}
        item['meesho_pid'] = meesho_pid
        item['product_link'] = url
        item['zipcode'] = pin_code
        item['pagesave_path'] = file_name

        obj.insert_data(item)

        obj.status_update(meesho_pid, pincode_flag)
        driver.quit()
    except:pass
