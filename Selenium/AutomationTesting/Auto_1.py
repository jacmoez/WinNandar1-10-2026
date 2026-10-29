from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge()

def open_browser():
    driver.get('https://testautomationpractice.blogspot.com/')
    driver.maximize_window()
    print('Test : Open Browser Success')
    time.sleep(2)

def inputs():
    input=driver.find_elements(By.CSS_SELECTOR,'input[placeholder^="Enter"]')
    print("All Inputs Count >> ",len(input))
    values=['Su Su','su@email.com','09998877']
    for i in range(len(input)):
        input[i].send_keys(values[i])
        time.sleep(1)
    driver.find_element(By.ID,'textarea').send_keys('Text Area')
    #radio
    driver.find_element(By.ID,'male').click()
    driver.find_element(By.ID,'female').click()
    days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    for dayId in days:
        driver.find_element(By.ID,dayId).click()
        # time.sleep(1)

    days=["sunday","thursday","friday","saturday"]
    for dayId in days:
        driver.find_element(By.ID,dayId).click()
        # time.sleep(1)
    select=Select(driver.find_element(By.ID,'country'))
    select.select_by_index(3) # 0
    time.sleep(1)
    select.select_by_value("australia")
    time.sleep(1)
    select.select_by_visible_text("India")  


    select=Select(driver.find_element(By.ID,'colors'))
    select.select_by_index(3) # 0
    time.sleep(1)
    select.select_by_value("green")
    time.sleep(1)
    select.select_by_visible_text("White") 

    select=Select(driver.find_element(By.ID,'animals'))
    select.select_by_index(3) # 0
    time.sleep(1)
    select.select_by_index(2) # 0
    time.sleep(1)
    select.select_by_index(4) # 0
    time.sleep(1)

    #date
    driver.find_element(By.ID,'datepicker').send_keys('10/29/2026')
    time.sleep(1)
    driver.find_element(By.ID,'txtDate').send_keys('10/29/2020',Keys.ENTER)
    time.sleep(1)
    dt1=driver.find_element(By.ID,'start-date')
    dt1.send_keys('10/29/2020')

    dt2=driver.find_element(By.ID,'end-date')
    dt2.send_keys('10/29/2026')

    driver.find_element(By.CLASS_NAME,'submit-btn').click()
    result=driver.find_element(By.ID,'result').text
    print(result)

    driver.find_element(By.ID,'singleFileInput').send_keys("C:\\Users\\NJ TECH\\Desktop\\1.jpg")
    driver.find_element(By.ID,'multipleFilesInput').send_keys("C:\\Users\\NJ TECH\\Desktop\\1.jpg","\n","C:\\Users\\NJ TECH\\Desktop\\img.png")
    



     
def main():
    open_browser()
    inputs()
    time.sleep(2)

main()
