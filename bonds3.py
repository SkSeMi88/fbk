import time

from bs4 import BeautifulSoup

import requests
from requests.exceptions import RequestException

import string

import json


url = "https://example.com"
url = "https://smart-lab.ru/q/bonds/"
url = "https://smart-lab.ru/q/ofz/"
url = "https://smart-lab.ru/q/bonds/order_by_val_to_day/desc/page"

columns = {
    0   :	["SECID"],
    1	:	["SHORTNAME"],
    2	:	["NAME"],
    3	:	["TYPENAME"],
    4	:	["ISIN"],
    5	:	["REGNUMBER"],
    6	:	["LISTLEVEL"],
    7	:	["FACEVALUE"],
    8	:	["FACEUNIT"],
    9	:	["ISSUESIZE"],
    10	:	["IS_COLLATERAL"],
    11	:	["IS_EXTERNAL"],
    12	:	["PRIMARY_BOARDID"],
    13	:	["PRIMARY_BOARD_TITLE"],
    14	:	["MATDATE"],
    15	:	["IS_RII"],
    16	:	["INCLUDEDBYMOEX"],
    17	:	["DURATION"],
    18	:	["IS_QUALIFIED_INVESTORS"],
    19	:	["HIGH_RISK"],
    20	:	["COUPONFREQUENCY"],
    21	:	["SUSPENSION_LISTING"],
    22	:	["EVENINGSESSION"],
    23	:	["MORNINGSESSION"],
    24	:	["WEEKENDSESSION"],
    25	:	["WAPRICE"],
    26	:	["YIELDATWAP"],
    27	:	["COUPONDATE"],
    28	:	["COUPONPERCENT"],
    29	:	["COUPONVALUE"],
    30	:	["COUPONDAYSPASSED"],
    31	:	["COUPONDAYSREMAIN"],
    32	:	["COUPONLENGTH"],
    33	:	["ISSUEDATE"],
    34	:	["INITIALFACEVALUE"],
    35	:	["SECSUBTYPE"],
    36	:	["STARTDATEMOEX"],
    37	:	["REPLBOND"],
    38	:	["DAYSTOREDEMPTION"],
    39	:	["OFFERDATE"],
    40	:	["EMITENTNAME"],
    41	:	["INN"],
    42	:	["LOTSIZE"],
    43	:	["PRICE"],
    44	:	["PRICE_RUB"],
    45	:	["RTL1"],
    46	:	["RTH1"],
    47	:	["RTL2"],
    48	:	["RTH2"],
    49	:	["RTL3"],
    50	:	["RTH3"],
    51	:	["DISCOUNT1"],
    52	:	["LIMIT1"],
    53	:	["DISCOUNT2"],
    54	:	["LIMIT2"],
    55	:	["DISCOUNT3"],
    56	:	["DISCOUNTL0"],
    57	:	["DISCOUNTH0"],
    58	:	["FULLCOVERED"],
    59	:	["FULL_COVERED_LIMIT"],
}


timestamp_ms = int(time.time() * 1000)
print(timestamp_ms)  # Например: 1712345678123
print()

# print(columns)

url = 'https://iss.moex.com/iss/apps/infogrid/emission/rates.json?_=1752432723860&start=0&limit=100'
url1 = 'https://iss.moex.com/iss/apps/infogrid/emission/rates.json'



try:
    url = url1 +'?_='+str(timestamp_ms)
    response = requests.get(url)
    response.raise_for_status()  # Вызовет исключение для 4XX/5XX статусов
    data = response.json()
    print(data.keys())
    # print(data["rates.cursor"]["data"][0][1])
    
    total_bonds = data["rates.cursor"]["data"][0][1]
    page_size   = data["rates.cursor"]["data"][0][2]
    pages       = total_bonds / page_size
    
    # количество страниц из общего числа бондов и размера страницы равным 100 строк
    quotient, remainder = divmod(total_bonds, page_size)
    
    pages = quotient + (1 if (remainder>0) else 0)
    
    print(pages)
    
    urls =[]
except RequestException as e:
    print(f"Ошибка при запросе: {e}")
except ValueError as e:
    print(f"Ошибка декодирования JSON: {e}")


print(pages)

page_size       = str(page_size)
array_of_pages  = []

result = []

for i in range(0, pages, 1):
    start =  str(i if (i==0) else (i)*100)
    print(start, i +1)
    # 1   0   0     100
    # 2   1   100   100
    # 3   2   200   100
    # 4   3   300   100

    
    try:
        url = url1 +'?_='+str(timestamp_ms) + "&start="+start+"&limit="+str(page_size)
        response = requests.get(url)
        response.raise_for_status()  # Вызовет исключение для 4XX/5XX статусов
        data = response.json()
        print(data.keys())
        
        result.extend(data["rates"]["data"])
        
        with open(str(i+1)+'.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)  # indent для красивого форматирования
        

    except RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except ValueError as e:
        print(f"Ошибка декодирования JSON: {e}")
        

data["rates"]["data"] = result
with open('merged.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(result.length())