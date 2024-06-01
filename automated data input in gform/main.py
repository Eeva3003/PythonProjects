from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#scraping link,address and price

header={
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" ,
        "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
}

response=requests.get("https://appbrewery.github.io/Zillow-Clone/",headers=header)

data=response.text
soup=BeautifulSoup(data,"html.parser")


#css selector

all_link_elements=soup.select("StyledPropertyCardDataWrapper a")

all_links=[link["href"] for link in all_link_elements]
print(f"There are{len(all_links)} links to individual listings in total/\n")
print(all_links)


#list of all addresses
all_addresses_element=soup.select(".StyledPropertyCardDataWrapper address")
all_addresses=[address.get_text().replace(" | ","").strip() for address in all_addresses_element]
print(f"\n after cleaning, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

# Create a list of all the prices on the page using a CSS Selector
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)


#FILL IN GOOGLE FORMS USING SELENIUM
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)


for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc6DANbnw4-XBYH1A4zp7H595DPAuk-s2fKJ-a3XIzfj6DYvg/viewform?usp=sf_link")
    time.sleep(2)
    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()




    #use xpath to select shprt answer fields
