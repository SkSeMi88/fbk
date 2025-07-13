import requests

url = "https://iss.moex.com/iss/statistics/engines/stock/markets/bonds/boards/TQCB/securities.json"
params = {
    "iss.meta": "off",
    "securities.columns": "SECID,SHORTNAME,COUPONVALUE,MATDATE,YIELD,ISSUESIZE"
}
response = requests.get(url, params=params)
print(response.text) 
# data = response.json()
# print(data["securities"]) #["data"])