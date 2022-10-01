from selenium import webdriver
from time import sleep
import time

email = "tulsyan.riya2811@gmail.com"
password = "28nov@1998"

driver = webdriver.Chrome(executable_path= r'C:\Users\SALESKEN\Desktop\workspace\chromedriver.exe')

driver.get("https://www.flipkart.com")
time.sleep(5000)
driver.find_element( "xpath","/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input" ).send_keys(email)
driver.find_element( "xpath","/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input" ).send_keys(password)
driver.find_element( "xpath","/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button" ).click()
driver.find_element( "xpath","/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input" ).click()

#driver.quit()
