import requests;
from bs4 import BeautifulSoup;
import smtplib
import time
#apple iphone 11 on flipkart.
while True :
 request = requests.get("https://www.flipkart.com/apple-iphone-11-white-128-gb/p/itme32df47ea6742?pid=MOBFWQ6B7KKRXDDS&lid=LSTMOBFWQ6B7KKRXDDSULUZ0N&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=organic&iid=7dde867f-82f3-4477-99e2-c11d1412722a.MOBFWQ6B7KKRXDDS.SEARCH&ppt=hp&ppn=homepage&ssid=aepr3x4454hu3uo01665116446204&qH=eb4af0bf07c16429")
 result= request.content
 soup = BeautifulSoup(result,'html.parser')
 price=float(soup.find('div',class_ ='_30jeq3 _16Jk6d').text[1:].replace(",",""))
 if(price < 60000) :
    smt = smtplib.SMTP('smtp.gmail.com',587)
    smt.ehlo()
    smt.starttls()
    time.sleep(5)
    # u can add your email here and 
    # note that this code will not work at the  time u see it
    # because i will change password.
    smt.login('rsanthoshreddy135@gmail.com','Santhosh@12345')
    time.sleep(5)
    smt.sendmail('rsanthoshreddy135@gmail.com','210050131@iitb.ac.in',f"Subject : Price Notifier\n\n Alert!! the price dropped to ${price},BUYIT!!.")
    smt.quit()
 time.sleep(24*60*60)
#<div class="_30jeq3 _16Jk6d">₹41,990</div>