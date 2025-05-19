
"""
    API 403 Forbidden Issue
    In these below all codes, I am testing on a site which gives 403 (forbidden) status at first request and then 200 in 2nd request
"""

# 1) Python solution that mimics browser behavior:
import requests
headers = {
    'authority': 'www.sofascore.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.sofascore.com',
    'pragma': 'no-cache',
    'referer': 'https://www.sofascore.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
# Use a session to maintain cookies
session = requests.Session()
# First make a request to the homepage to establish session
homepage_url = 'https://www.sofascore.com/'
session.get(homepage_url, headers=headers)
# Now make your API request
api_url = 'https://www.sofascore.com/api/v1/event/12436535/team-streaks'
response = session.get(api_url, headers=headers)
print(response.status_code)
print(response.json())

# ///////////////////////////////////////////////////////////////////////////////////////////

# 2) If site uses  Cloudflare, then you might need more advanced tools like cloudscraper
import cloudscraper
scraper = cloudscraper.create_scraper()
response = scraper.get(api_url)

# ///////////////////////////////////////////////////////////////////////////////////////////

# 3) If site has likely implemented more advanced bot protection
import requests
headers = {
    'authority': 'www.sofascore.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
cookies = {
    'deviceId': 'some_random_device_id',
    'sessionId': 'some_random_session_id',
}
session = requests.Session()
# 1. First make a HEAD request to bypass initial protection
session.head('https://www.sofascore.com/', headers=headers)
# 2. Then make the actual request with proper cookies
api_url = 'https://www.sofascore.com/api/v1/event/12436535/team-streaks'
response = session.get(api_url, headers=headers, cookies=cookies)
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print(response.json())
else:
    print(f"Response Text: {response.text}")

# ////////////////////////////////////////////////////////////////////////////////////////////

# 4) for Cloudflare protected websites
# -----------------------
# 4.1) cloud scraper
import cloudscraper
scraper = cloudscraper.create_scraper()
response = scraper.get('https://www.sofascore.com/api/v1/event/12436535/team-streaks')
print(f"Status Code: {response.status_code}")

# ------------------------
# 4.2) Try Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.sofascore.com/event/12436535")
api_url = driver.execute_script("return fetch('https://www.sofascore.com/api/v1/event/12436535/team-streaks').then(r => r.json())")
print(api_url)

# ///////////////////////////////////////////////////////////////////////////////////////////

# 5) If site is likely using advanced anti-bot mechanisms (such as Cloudflare, PerimeterX, or custom fingerprinting
# ------------------------
# 5.1) Use requests-impersonate (Mimics Real Browser Traffic)
from pyreqwest_impersonate import chrome
# Use Chrome browser impersonation
session = chrome("latest")  # Uses latest Chrome version
url = "https://www.sofascore.com/api/v1/event/12436535/team-streaks"
response = session.get(url)
print(response.status_code)  # Should be 200
print(response.json())  # Should return the data

# ----------------------
# 5.2) Use curl_cffi (Bypasses Cloudflare & Anti-Bot)
from curl_cffi import requests
headers = {
    "Accept": "*/*",
    "Referer": "https://www.sofascore.com/",
}
response = requests.get(
    "https://www.sofascore.com/api/v1/event/12436535/team-streaks",
    headers=headers,
    impersonate="chrome110" 
)
print(response.status_code)  
print(response.json()) 

# ---------------------
# 5.3) Use Selenium with Undetected ChromeDriver (If API-level requests are blocked, automate a real browser instead.)
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
options = uc.ChromeOptions()
options.add_argument("--headless=new")  # Run in background (remove if debugging)
driver = uc.Chrome(options=options)
try:
    # Load a dummy page first (to set cookies)
    driver.get("https://www.sofascore.com/")
    time.sleep(2)  # Let anti-bot checks pass
    # Now fetch the API data using JavaScript
    api_url = "https://www.sofascore.com/api/v1/event/12436535/team-streaks"
    script = f"""
    fetch("{api_url}")
        .then(response => response.json())
        .then(data => window.apiData = data)
    """
    driver.execute_script(script)
    time.sleep(2)  # Wait for API response
    # Extract the data
    api_data = driver.execute_script("return window.apiData;")
    print(api_data)  # Should contain the response
finally:
    driver.quit()