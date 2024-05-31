from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


SIMILAR_ACCOUNT=WANT TO FOLLOW
USERNAME="eeva.eldhose@gmail.com"
PASSWORD="Instagram@2003"

class InstaFollower:
    def __init__(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=chrome_options)

    def login(self):
        url="https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning=self.driver.find_element(By.XPATH,decline_cookies_xpath)

        if cookie_warning:
            cookie_warning[0].click()

        username=self.driver.find_element(by=By.NAME,value="username")
        password=self.driver.find_element(by=By.NAME,value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)

        #not now and ignore
        save_login_prompt=self.driver.find_element(by=By.PATH,value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        #not now
        notification_prompt=self.driver.find_element(by=By.XPATH,value="// button[contains(text(), 'Not Now')]")
        if notification_prompt:
            notification_prompt.click()
    def find_follower(self):
        time.sleep(5)
        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        pass

bot=InstaFollower()
bot.login()
bot.find_follower()
bot.follow()
