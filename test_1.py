from playwright.sync_api import sync_playwright

num_windows = 5
url = "https://www.example.com"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    for _ in range(num_windows):
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

    browser.close()
