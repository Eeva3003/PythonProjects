from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
ACC_EMAIL="eeva.eldhose@gmail.com"
ACC_PASS="Aurora@2003"
PHONE=9887807085

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3839975677&f_E=1&f_WT=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
''''#clicking reject cookies button
time.sleep(2)
reject_button=driver.find(by=By.CSS_SELECTOR,value='button[action-type="DENY"]')
reject_button.click()'''

#to click sign in
time.sleep(2)
sign_in_button=driver.find_element(by=By.LINK_TEXT,value="Sign in")
sign_in_button.click()

#sign in using ur emal and password
time.sleep(5)
email_box=driver.find_element(by=By.ID,value="username")
email_box.send_keys(ACC_EMAIL)
pass_box=driver.find_element(by=By.ID,value="password")
pass_box.send_keys(ACC_PASS)
pass_box.send_keys(Keys.ENTER)

#captcha
input("press enter when u have solved the captcha")

 Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
