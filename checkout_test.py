from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import LOGIN_CREDENTIALS, CHECKOUT_INFO
from login_test import login,chrome
#navigator

driver = chrome()
wait = WebDriverWait(driver, 5)  
      
try:
    login(driver,wait)


    add_item_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_item_btn.click()
        
        
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    wait.until(EC.url_contains("cart.html"))
    print("cart")
        
    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    first_name.send_keys(CHECKOUT_INFO["valid"]["first_name"])

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys(CHECKOUT_INFO["valid"]["last_name"])

    zipcode = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
    zipcode.send_keys(CHECKOUT_INFO["valid"]["zipcode"])

    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

    finish_btn = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    finish_btn.click()

    thankyou = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='complete-header' and contains(text(), 'Thank you')]")))
    #wait.until(EC.url_contains("checkout-complete.html"))
    print("Checkout successful!")
    
except Exception as e:
    print(f"login failed: {str(e)}")
    driver.save_screenshot("error.png")

finally:
    driver.quit()
