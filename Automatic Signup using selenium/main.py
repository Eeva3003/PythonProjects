from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
fname=driver.find_element(By.NAME,value="fName")
lname=driver.find_element(By.NAME,value="lName")
email=driver.find_element(By.NAME,value="email")

fname.send_keys("Eeva")
lname.send_keys("Eldhose")
email.send_keys("abc@gmail.com")

signup=driver.find_element(By.CSS_SELECTOR,value="form button")
signup.click()
#driver.close()
