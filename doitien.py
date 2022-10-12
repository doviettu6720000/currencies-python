from tkinter import Y
import requests
import json
from pprint import pprint

def getJsondata(fileName,key):
    file = open(fileName)
    data = json.load(file)
    return data[key]

api_key = getJsondata('api.json','API_KEY')
url = "http://data.fixer.io/api/latest?access_key=" + api_key
dataURL = requests.get(url).text
dataJson = json.loads(dataURL)
dataRates = dataJson["rates"]

currencies = getJsondata('currencies.json','currencies')
def CurrencyConvert():
    query = input("Xem bang tien te ? (Y/N): ").upper()
    if query == "Y":
        pprint(currencies)

    amount = float(input("Nhap so tien: "))
    fromCurrency = input("Nhap don vi doi hien tai: ").upper()
    toCurrency = input("Nhap don vi hoan thanh: ").upper()
    convertAmount = round(amount * dataRates[toCurrency] / dataRates[fromCurrency],2)
    print(f"{amount} {fromCurrency} = {convertAmount} {toCurrency}")

try:
    CurrencyConvert()
except:
    print("Wrong input!")
    CurrencyConvert







