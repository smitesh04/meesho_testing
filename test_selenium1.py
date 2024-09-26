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


# Initialize the driver
driver = uc.Chrome(options=options, driver_executable_path=chromedriver_path)

try:
    driver.get("https://www.meesho.com/auth?redirect=https%3A%2F%2Fwww.meesho.com%2F&source=profile&entry=header&screen=HP/")

    # Wait for the phone number input to be clickable
    wait = WebDriverWait(driver, 20)
    input_tel = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="tel"]')))
    input_tel.click()

    # Enter phone number
    input_tel.send_keys("6353677936")  # Replace with your phone number

    # Wait for and click the submit button
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    submit.click()

    # Wait for a while after submission
    time.sleep(40)  # Adjust if necessary
    # otp = input("enter otp")
    # otp_list = [i for i in otp]
    #
    # c = 1
    # for j in otp_list:
    #
    #     wait = WebDriverWait(driver, 20)
    #     input_otp = wait.until(EC.element_to_be_clickable((By.XPATH, f'//input[@type="tel"][{c}]')))
    #     input_otp.click()
    #
    #     # Enter phone number
    #     input_otp.send_keys(j)
    #     c += 1

    # submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    # submit.click()

    # Save cookies to a file
    with open("cookies.pkl", "wb") as file:
        pickle.dump(driver.get_cookies(), file)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the browser is closed
    driver.quit()
