from selenium   import  webdriver
from selenium.webdriver.common.by import By
import time
class SauceDemo:
    def __init__(self):
        self.driver=webdriver.Edge()
    def open_browser(self):
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        time.sleep(3)
    def login(self):
        users=[
            {'username':'','password':''},
            {'username':'QA','password':''},
            {'username':'','password':'123'},
            {'username':'QA','password':'123'},
            {'username':'standard_user','password':'secret_sauce'},
        ]
        for user in users:
            username=user['username']
            password=user['password']
            self.driver.find_element(By.ID,'user-name').send_keys(username)
            self.driver.find_element(By.ID,'password').send_keys(password)
            time.sleep(2)
            self.driver.find_element(By.ID,'login-button').click()
            if not (username=="standard_user" and password=="secret_sauce"):
                error=self.driver.find_element(By.TAG_NAME,'h3').text
                print(error)
            self.driver.refresh()
            time.sleep(2)




    def main(self):
        self.open_browser()
        self.login()

SauceDemo().main()
