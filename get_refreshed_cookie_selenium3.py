import pickle
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from fake_useragent import UserAgent
chromedriver_path = r"C:\Users\Actowiz\Downloads\chromedriver-win64\chromedriver.exe"
chrome_executable_path = r"C:\Users\Actowiz\Downloads\chrome-win64\chrome.exe"
# User agent
ua = UserAgent()

# Set up undetected Chrome options
options = uc.ChromeOptions()
# options.add_argument('--headless')  # Uncomment for headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(f"user-agent={ua.random}")
options.binary_location = chrome_executable_path
# service = Service(executable_path=chromedriver_path)

def refresh_cookie_pkl(url, cookies_pkl):

    # Initialize the driver
    driver = uc.Chrome(options=options, driver_executable_path=chromedriver_path)

    try:
        driver.get(url)
        # Load cookies from the file
        with open(cookies_pkl, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        # Refresh the page to reflect the loaded cookies
        driver.refresh()
        # Optional: Wait for a while to see the result
        time.sleep(10)

        # Save cookies to a file
        with open(cookies_pkl, "wb") as file:
            pickle.dump(driver.get_cookies(), file)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the browser is closed
        driver.quit()



if __name__ == '__main__':
    url = 'https://www.meesho.com/'
    flag = True
    while flag:
        cookies_pkls = [
            'cookies.pkl',
            'cookies2.pkl',
            'cookies3.pkl',
            'cookies4.pkl',
        ]

        for cookie_pkl in cookies_pkls:
            # cookies_pkl = 'cookies3.pkl'
            refresh_cookie_pkl(url=url, cookies_pkl=cookie_pkl)

            time.sleep(300)

