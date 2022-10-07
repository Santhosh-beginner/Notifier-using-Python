import requests;
from bs4 import BeautifulSoup;
import smtplib
import time
#book item on booktoscrape.com.
while True :
 request = requests.get("https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html")
 result= request.content
 soup = BeautifulSoup(result,'html.parser')
 price=float(soup.find('p',class_ ='price_color').text[1:].replace(",",""))
 print(price)
 if(price < 60) :
    smt = smtplib.SMTP('smtp.gmail.com',587)
    smt.ehlo()
    smt.starttls()
    # u can add your email here and 
    # note that this code will not work at the  time u see it
    # because i will change password.
    smt.login('rsanthoshreddy135@gmail.com','Santhosh@12345')
    smt.sendmail('rsanthoshreddy135@gmail.com','210050131@iitb.ac.in',f"Subject : Price Notifier\n\n Alert!! the price dropped to ${price},BUYIT!!.")
    smt.quit()
 time.sleep(24*60*60)