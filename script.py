import argparse
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager


def import_driver():
    webdriver_options = Options()
    webdriver_options.add_argument('--headless')
    webdriver_options.add_argument("--incognito")
    webdriver_options.add_argument('--no-sandbox')
    webdriver_options.add_argument('--disable-dev-shm-usage')
    webdriver_options.add_argument('--disable-gpu')
    webdriver_options.add_argument('--disable-blink-features=AutomationControlled')
    webdriver_options.add_argument(
        '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    )

    webdriver_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    webdriver_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=webdriver_options, service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    stealth(
        driver=driver,
        languages=['ko-KR', 'ko'],
        vender='Google Inc',
        platform='MacIntel',
        webgl_vendor='Intel Inc',
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True
    )

    return driver


if __name__ == '__main__':
    URL = 'https://everytime.kr/370438/v/361066893'

    everytime_id = 'go2033302'
    everytime_password = '00donguk00@#'
    ANTICAPTCHA_API_KEY = 'a710d056b34ea7edf41c75df097ae37f'

    driver = import_driver()
    print("[Done ] initialize driver.")

    # Check url
    pattern = r'^https://everytime\.kr/(\d+)/v/(\d+)$'
    match = re.match(pattern, URL)
    if not match:
        print("[Error] unvalid url."); exit()
    else:
        group, article = match.groups()
    
    # Login
    driver.get(f'https://account.everytime.kr/login?redirect_uri=https%3A%2F%2Feverytime.kr%2F{group}%2Fv%2F{article}')
    print(driver.current_url)
    print(driver.get_log("browser"))

    id_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "id"))
    )
    id_field.send_keys(everytime_id)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys(everytime_password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
    )
    login_button.click()

    with open('temp3.txt', 'w') as file:
        file.write(str(driver.page_source))

    print("[Done ] Login.")
    print(driver.current_url)
    print(driver.get_log("browser"))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "large")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    large_h2_tags = soup.find_all('h2', class_='large')
    large_p_tags = soup.find_all('p', class_='large')

    for h2 in large_h2_tags:
        print(h2.get_text(strip=True))

    for p in large_p_tags:
        print(p.get_text(strip=True))