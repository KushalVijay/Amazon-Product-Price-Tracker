import bs4
import requests
import smtp,time

url = "Url_to_the_product"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

#Scraping the data according the url provided
def check_price():
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    conerted_price = float(price)

    if(converted_price < "Your budget"):
        send_mail()

    print(converted_price)
    print(title.strip())


#Sending Mail using Gmail
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Your_Gmail_id','Password')

    subject = 'Price fell down!!!'
    body = 'Check the amazon link to buy'+url

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "sender_email",
        "receiver_email",
        msg
        )
    print("Mail has been sent")
    server.quit()

#Function Call
check_price()
