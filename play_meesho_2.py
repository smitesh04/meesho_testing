import datetime
import hashlib
import os
import sys
import time

import pymysql
from playwright.sync_api import sync_playwright
from browserforge.fingerprints import FingerprintGenerator
from browserforge.injectors.playwright import NewContext

# Global variable to track login status and processing completion
login_successful = False
processing_complete = False

connect = pymysql.connect(
    host='172.27.131.60',
    user='root',
    password='actowiz',
    database='meesho_master'
)
cursor = connect.cursor()

local_connect = pymysql.connect(
    host='localhost',
    user='root',
    password='actowiz',
    database='meesho_page_save'
)
local_cursor = local_connect.cursor()


def product_page_traffic(response, url, url_id, pincode):
    global processing_complete
    if 'check-shipping' in response.url:
        print(f"Shipping response received from: {response.url}")
        # Generate a hash ID based on the URL
        page_id = hashlib.sha256((url + f'_{pincode}').encode()).hexdigest()
        today_date = datetime.datetime.today().strftime("%d_%m_%Y")

        # Writing response to a file with a unique name using the hash ID
        with open(fr'C:\Users\Actowiz\Desktop\pagesave\meesho\{today_date}\{page_id}.html', 'w') as file:  # EDIT THIS
            file.write(response.text())
        # Mark processing as complete once the file is written
        update_query = f"""UPDATE product_links_20240920 SET status_{pincode}='Done' WHERE id={url_id}"""
        cursor.execute(update_query)
        connect.commit()

        insert_query = f"""INSERT INTO pages (url, pincode, page_hash) VALUES ('{url}', '{pincode}', '{page_id}')"""
        local_cursor.execute(insert_query)
        local_connect.commit()
        processing_complete = True


def navigate_to_product(url, page, url_id, pincode):
    global processing_complete

    # Wrapper function to include the URL in the response handler
    def handle_response(response):
        product_page_traffic(response, url, url_id, pincode)

    page.on('response', handle_response)

    # Navigate to product URL
    page.goto(url, timeout=10000)

    try:
        pincode_fail = None
        # XPath of the element to check
        xpath = '//input[@id="pin"]'
        # Check if the element exists and is visible within 5 seconds
        element = page.locator(xpath)
        element.wait_for(state='visible', timeout=5000)  # Wait for max 5 seconds

        out_of_stock = False
        # Further processing if element exists
        print("Element found and is visible, proceeding with actions.")
        element.fill(str(pincode)) # Fill in the input field
        page.locator('//button[@color="pinkBase"]//span[contains(text(), "CHECK")]').click()  # Click the button

        # Check if the specific error popup appears after clicking the button
        popup_locator = page.locator('//*[contains(text(), "Pincode request failed")]')
        try:
            # Wait for the error popup to appear, max 2 seconds
            popup_locator.wait_for(state='visible', timeout=2000)
            print("Pincode request failed popup detected, skipping.")
            pincode_fail = True
            sys.exit("Pincode request failed. Exiting.")
        except:
            pincode_fail = False
            # No popup detected, continue with the rest of the logic
            print("No popup detected, continuing with further actions.")

    except Exception:
        out_of_stock = True
        pincode_fail = True
        # Skip this element if it's not found or not visible within 2 seconds
        print("Element not found or not visible within 2 seconds. Skipping this step.")
        update_query = f"""UPDATE product_links_20240920 SET status_{pincode}='Done' WHERE id={url_id}"""
        cursor.execute(update_query)
        connect.commit()

    if not out_of_stock and not pincode_fail:
        # Wait until the product_page_traffic finishes processing (file is written)
        while not processing_complete:
            time.sleep(1)  # Check every second if processing is complete

    # Once the file is written, close the tab
    page.close()

    # Reset for the next product
    processing_complete = False


def login(page, context):
    global login_successful
    login_successful = False

    def login_handle_traffic(response):
        global login_successful
        if 'verify.json' in response.url:
            print(f"Login verification response received from: {response.url}")
            login_successful = True

    # Listen to all network responses
    page.on('response', login_handle_traffic)

    # Navigate to the login page
    page.goto('https://www.meesho.com/auth')

    # Fill mobile number
    page.locator('//input[@type="tel"]').fill('6353677936')  # EDIT THIS
    page.locator('//button[@type="submit"]').click()

    # Wait for the user to input the OTP
    otp = input('Enter OTP: ')
    for index in range(len(otp)):
        page.locator(f'//input[@type="tel"][{index + 1}]').fill(otp[index])

    # Wait for the login process to complete
    time.sleep(5)

    # Save cookies after successful login
    if login_successful:
        context.storage_state(path="session_storage.json")  # Save session cookies

    return login_successful


def main(pincode, start_id, end_id):
    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=True)

        fingerprints = FingerprintGenerator()
        fingerprint = fingerprints.generate()

        # Use saved cookies/session data if exists
        if os.path.exists('session_storage.json'):
            context = NewContext(browser, fingerprint=fingerprint, storage_state="session_storage.json")
            query = f"""SELECT id, meesho_pid FROM product_links_20240920 WHERE status='Done' AND status_{pincode} != 'Done' AND id BETWEEN {start_id} AND {end_id} """
            cursor.execute(query)
            rows = list(cursor.fetchall())

            # Process URLs one by one
            for row in rows:
                url_id = row[0]
                pid = row[1]
                url = f'https://www.meesho.com/s/p/{pid}'
                page = context.new_page()
                navigate_to_product(url, page, url_id, pincode)

        else:
            fingerprints = FingerprintGenerator()
            fingerprint = fingerprints.generate()

            context = NewContext(browser, fingerprint=fingerprint)  # Create a single browser context

            # Perform login on the first tab
            page = context.new_page()
            logged_in = login(page, context)

            if logged_in:
                print("Login successful!")
            else:
                print("Login failed or no response detected!")

        browser.close()


if __name__ == '__main__':
    try:
        pincode = int(sys.argv[1])
        start_id = int(sys.argv[2])
        end_id = int(sys.argv[3])
    except:
        pincode = '400001'
        start_id = 1333
        end_id = 5555
    main(pincode=pincode, start_id=start_id, end_id=end_id)
