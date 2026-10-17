from selenium   import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
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
            time.sleep(1)

    def products(self):
        assert "Products" in self.driver.page_source
        
        titles=[
            'Sauce Labs Backpack',
            'Sauce Labs Bike Light',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Fleece Jacket',
            'Sauce Labs Onesie',
            'Test.allTheThings() T-Shirt (Red)'
        ]
        for title in titles:
            self.driver.find_element(By.LINK_TEXT,title).click()
            detail_title=self.driver.find_element(By.CLASS_NAME,'inventory_details_name').text
            print(detail_title)
            time.sleep(1)
            self.driver.back()
            time.sleep(1)
        time.sleep(3)

    def add_to_cart(self):
        ids=[
            'add-to-cart-sauce-labs-backpack',
            'add-to-cart-sauce-labs-bike-light',
            'add-to-cart-sauce-labs-bolt-t-shirt',
            'add-to-cart-sauce-labs-fleece-jacket',
            'add-to-cart-sauce-labs-onesie',
            'add-to-cart-test.allthethings()-t-shirt-(red)'
        ]
        for id in ids:
            self.driver.find_element(By.ID,id).click()
            time.sleep(1)

        remove_ids=[
                    'remove-sauce-labs-bike-light',
                    'remove-sauce-labs-onesie'
                ]
        for id in remove_ids:
            self.driver.find_element(By.ID,id).click()
            time.sleep(1)
    def sort_product(self):
        select_el=self.driver.find_element(By.CLASS_NAME,'product_sort_container')
        select=Select(select_el)
        select.select_by_index(1)
        time.sleep(1)
        select_el=self.driver.find_element(By.CLASS_NAME,'product_sort_container')
        select=Select(select_el)
        select.select_by_value('lohi')
        time.sleep(1)
        select_el=self.driver.find_element(By.CLASS_NAME,'product_sort_container')
        select=Select(select_el)
        select.select_by_visible_text('Price (high to low)')

    def view_cart(self):
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        item_names=self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        for item in item_names:
            print('Item Name : ',item.text)
        self.driver.find_element(By.ID,'checkout').click()
       
    def checkout_info(self):
        self.driver.find_element(By.ID,'first-name').send_keys('QA Engineer')
        self.driver.find_element(By.ID,'last-name').send_keys('Test')
        self.driver.find_element(By.ID,'postal-code').send_keys('112233')
        self.driver.find_element(By.ID,'continue').click()
        time.sleep(2)
    def checkout_overview(self):
        price_els=self.driver.find_elements(By.CLASS_NAME,'inventory_item_price')
        item_total=0
        for price_el in price_els:
            price_text=price_el.text
            print(price_text)
            item_total+=float(price_text.strip('$'))
        print('Item total : ',item_total) 
        #Item total: $79.95
        summary_subtotal=float(self.driver.find_element(By.CLASS_NAME,'summary_subtotal_label').text.strip('Item total: $'))
        print('Summary Total : ',summary_subtotal)
        assert  item_total==summary_subtotal
        tax=float(self.driver.find_element(By.CLASS_NAME,'summary_tax_label').text.strip('Tax: $'))
        print('Tax : ',tax)
        summary_total=float(self.driver.find_element(By.CLASS_NAME,'summary_total_label').text.strip('Total: $'))
        print('Tax : ',summary_total)
        
        added_total=summary_subtotal+tax
        print(summary_total,float("%.2f"%added_total))
        assert summary_total==float("%.2f"%added_total)
        self.driver.find_element(By.ID,'finish').click()
    def logout(self):
        self.driver.find_element(By.ID,'react-burger-menu-btn').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="logout_sidebar_link"]').click()
    def main(self):
        self.open_browser()
        self.login()
        self.products()
        self.add_to_cart()
        self.sort_product()
        self.view_cart()
        self.checkout_info()
        self.checkout_overview()
        self.logout()
        time.sleep(3)

SauceDemo().main()
