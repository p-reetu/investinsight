from celery import shared_task
from bs4 import BeautifulSoup
import requests
from .models import GoldRates

@shared_task
def fetch_gold_price():
    try:
        url = "https://groww.in/gold-rates"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36'}
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        goldRateText = soup.find_all('tr',class_="bodyBase")[7].find_all('div')[0].find('div').get_text(strip=True).replace(',',"").replace('₹',"")
        goldRateValue = float(goldRateText)
        GoldRates.objects.create(rate=goldRateValue)
        print("Gold price fetched and saved!")
    except Exception as e:
        print("Error in fetching gold rate " , e)