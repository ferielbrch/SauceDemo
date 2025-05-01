from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import LOGIN_CREDENTIALS

#navigator
def chrome():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless") #without graphical interface
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

driver = chrome()

try:
    #load websitee
    website = 'https://www.saucedemo.com/'
    driver.get(website)
    wait = WebDriverWait(driver, 5)    

    #login
    username = driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')        
    username.send_keys(LOGIN_CREDENTIALS["valid"]["username"])

    password = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    password.send_keys(LOGIN_CREDENTIALS["valid"]["password"])

    login_button = driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')
    login_button.click()

    wait.until(EC.url_contains("inventory.html"))
    print("Login successful!")
        
except Exception as e:
    print(f"login failed: {str(e)}")
    driver.save_screenshot("error.png")

finally:
    driver.quit()
