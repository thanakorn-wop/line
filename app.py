from flask import Flask, request
import requests
from parinya import LINE
import cv2
import time 
from datetime import date
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
app = Flask(__name__)
@app.route("/")
def hello():
    localtime = time.asctime( time.localtime(time.time()) )
    def covide():
        line  = LINE("V7HAdVkbNrFqdYYieUkrLwWd9aGmnAKMyklvcDwQHYc")
        response = requests.get("https://covid19.th-stat.com/api/open/today")
        data = response.json()
    
        today = date.today()
        noti = 'รายงานสถาณการ์ณโควิดของวันที่ '+str(today)+'\n'
        new_cofirm = "ผู้ติดเชื้อใหม่ = "+str(data["NewConfirmed"])
        confirm = "\nยอดสะสม = "+ str(data["Confirmed"])
        recover = "\nหายแล้ว = "+str(data["Recovered"])
        hospital = "\nรักษาตัวใน รพ. = "+str(data["Hospitalized"])
        deaths = "\nเสียชีวิตรวม = "+str(data["Deaths"])
        new_deaths = "\nเสียชีวิตเพิ่ม  = "+str(data["NewDeaths"])
        line.sendtext(noti+new_cofirm+confirm+recover+hospital+deaths+new_deaths)
    def gold():
        line  = LINE("V7HAdVkbNrFqdYYieUkrLwWd9aGmnAKMyklvcDwQHYc")
        url = "https://www.goldtraders.or.th/"
        url = requests.get(url)
        url.encoding = 'utf-8'
        soup = BeautifulSoup(url.text,'lxml')
        # find = soup.find(id = "vue-app")
        # print(soup)
        # print(find)

        time = soup.find(id = "DetailPlace_uc_goldprices1_lblAsTime").text
        sell_96 = soup.find(id = "DetailPlace_uc_goldprices1_lblBLSell").text
        sell = soup.find(id = "DetailPlace_uc_goldprices1_lblOMSell").text
        buy_96 = soup.find(id = "DetailPlace_uc_goldprices1_lblBLBuy").text
        buy = soup.find(id = "DetailPlace_uc_goldprices1_lblOMBuy").text
        # buy_sell = {"ราคาซื้อ":[buy_96,buy],"ราคาขาย":[sell_96,sell]}
        gold99  = time+"\n( ทองคำแท่ง 96.5%  รับซื้อ "+ buy_96 +" ขาย " + sell_96+ ")"+","+" ทองคำรูปพรรณ 96.5%  รับซื้อ "+ buy + " ขาย " + sell +")"
        # line.sendtext(pd.DataFrame(buy_sell, index=["ทองคำแท่ง 96.5% ", "ทองคำรูปพรรณ 96.5% "]))
        line.sendtext(gold99)

    gold()
    covide()
    return "Hello 1111Guys!"


@app.route("/webhook")
def webhook():
    return 'OK'
    
if __name__ == "__main__":
    app.run()