import argparse
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def import_driver():
    webdriver_options = Options()
    webdriver_options.add_argument('--headless')
    webdriver_options.add_argument("--incognito")
    webdriver_options.add_argument('--no-sandbox')
    webdriver_options.add_argument('--disable-dev-shm-usage')
    webdriver_options.add_argument('--disable-gpu')
    webdriver_options.add_argument(
        '--user_agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    )
    
    driver = webdriver.Chrome(options=webdriver_options)
    driver.implicitly_wait(10)

    return driver


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', type=str, required=True, help='everytime post url')
    args, _ = parser.parse_known_args()

    everytime_id = 'go2033302'
    everytime_password = '00donguk00@#'

    driver = import_driver()
    print("[Done ] initialize driver.")

    # Check url
    pattern = r'^https://everytime\.kr/(\d+)/v/(\d+)$'
    match = re.match(pattern, args.url)
    if not match:
        print("[Error] unvalid url."); exit()
    else:
        group, article = match.groups()
    
    # Login
    driver.get(f'https://account.everytime.kr/login?redirect_uri=https%3A%2F%2Feverytime.kr%2F{group}%2Fv%2F{article}')
    print(driver.current_url)

    print(driver.get_log("browser"))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "id"))).send_keys(everytime_id)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(everytime_password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))).click()

    print("[Done ] Login.")

