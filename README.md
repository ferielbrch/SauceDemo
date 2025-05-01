# SauceDemo Automation

This project contains automated end-to-end tests for the SauceDemo web application using Selenium and Python.  
It covers two main scenarios: login validation and the full checkout workflow.

# Structure of the project

sauce_automation/  
├── config.py               # Test data configuration  
├── checkout_test.py        #Checkout test script  
└── login_test.py        #login test script  

# Requirements

- Python 3.10
- Google Chrome browser
- ChromeDriver 

# Steps to execute
1. Clone repo
```bash
git clone https://github.com/ferielbrch/SauceDemo.git
cd SauceDemo
```
2. Install dependencies: 

```bash
   pip install selenium webdriver-manager
   ```
3. Configure test data in 'config.py' :
```python
   LOGIN_CREDENTIALS = {
       "valid": {
           "username": "standard_user",
           "password": "secret_sauce"
       }
   }
   ```
4. Running tests:
Execute the test script:
```bash
python login_test.py
python checkout_test.py
```
## Scenarios
1. **Login test**
    - Test valid credentials authentication
    - Verify inventory page redirection

2. **Checkout Flow**
    - Add item to cart
    - Check cart content
    - Checkout
    - Fill shipping details
    - Finish

# EXPECTED OUTPUT 
1. SUCCESS
```
Login successful!
Checkout successful!
```

2. FAILURE
    - Screenshot saved as `error.png`
    - Error message in console

# Tools & Frameworks
    - Selenium Webdriver
    - Python