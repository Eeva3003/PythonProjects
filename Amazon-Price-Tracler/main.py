from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
YOUR_EMAIL=" "
YOUR_PASSWORD=" "
AMAZON_URL="https://www.amazon.in/Laneige-Sleeping-Moisturizing-Vitamin-Antioxidant/dp/B0BPC8KG73/ref=sr_1_5?crid=3TK4RDBANQ8AR&dib=eyJ2IjoiMSJ9.ntA-yrA7qTN1xiu4DpYWzxEeLxmlRKDPTFCl45UQFSwWh8gNKTW0cmlsPNpSkEI01TAgY2QaV_ArIhMrf_yClkuvs2eDFrCBy_i4hUBakjGrpTSSkEH52UXEUi0DOt3DKYqeoc91c7BRhYEvCNLyBPwPi4vX69nRAQEbs3EXyR-hSr0WANyxHqV5-B--deR1mapUpYm0UbsjmHpuf7uIACg3dyX91zzKXeT1fvomjEJBddQ4Jf1AyJFQc4H-e_VORxy59z_-02Ar-f6v_ptrEEDCTwNSy9AKoHzFfCIYuug.Q6nykFbkDoye8UQ9SYYlL0711XqBeb-zkHecXMF4Qm4&dib_tag=se&keywords=laneige&qid=1716894898&sprefix=laneige+%2Caps%2C241&sr=8-5"
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
ACCEPT_LANG="en-GB,en-US;q=0.9,en;q=0.8"


r=requests.get(AMAZON_URL, headers={"User-Agent":USER_AGENT,"Accept-Language":ACCEPT_LANG})
soup=BeautifulSoup(r.content,"lxml")
print(soup.prettify())

price=soup.find(class_="aok-offscreen").get_text()
price_without_currency=price.split("₹")[1]
parts = price_without_currency.split()
number_part = parts[0].split('.')[0]
price_float=float(number_part)
print(price_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 400

if price_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_URL}".encode("utf-8")
        )

