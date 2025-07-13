# # The line `# import requests` is a comment in Python code. Comments are used to provide explanations
# # or notes within the code for developers to understand the purpose of certain sections of code. In
# # this case, the comment indicates that the `requests` module is typically imported in Python for
# # making HTTP requests, but it seems that it is not being used in the provided code snippet.
# import requests

# from bs4 import BeautifulSoup

# url = "https://smart-lab.ru/q/bonds/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# rows = soup.select("table#bonds_list tr")[1:]  # пропускаем заголовок
# for row in rows:
#     cells = row.select("td")
#     name = cells[0].get_text(strip=True)
#     ticker = cells[1].get_text(strip=True)
#     price = cells[2].get_text(strip=True)
#     yield_to_maturity = cells[3].get_text(strip=True)
#     print(f"{ticker} | {name} | Цена: {price} | Доходность: {yield_to_maturity}")
#     print()



from bs4 import BeautifulSoup 
import requests
import string


url = "https://example.com"
url = "https://smart-lab.ru/q/bonds/"
url = "https://smart-lab.ru/q/ofz/"
url = "https://smart-lab.ru/q/bonds/order_by_val_to_day/desc/page"



t_cells = [
    "№",
    "Имя",
    "Ссылка",
    "Лет до погаш.",
    "Доходн",
    "Год.куп. дох.",
    "Куп.дох.посл.",
    "Рейтинг",
    "Объем, млн руб",
    "Купон, руб",
    "Частота,раз в год",
    "НКД, руб",
    "Дюр-я, лет",
    "Цена",
    "Дата купона",
    "Размещение",
    "Погашение",
    "Оферта",
]

DOMEN = "https://smart-lab.ru"

# проходим каждую страницу таблицу - всего их 19 проверили вручную через ">>"
for i in range(1, 20, 1):
    URL = url+str(i)+"/"
    # print(URL);
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)  # Prints the page's <title> tag

    rows = soup.select("table  tr")[1:]  # пропускаем заголовок

    for row in rows:
        
        # print(row)
        cells = row.select("td")
        
        line = ""
        # for cell in cells:
        # for cell in range(1,19,1):
        line += f"{cells[0].get_text(strip=True)} |"
        line += f"{cells[1].get_text(strip=True)} |"
        line += f"{DOMEN}{cells[1].find('a').get('href')} |" if (cells[1].find('a')) else "|"
        line += f"{DOMEN}{cells[2].find('a').get('href')} |" if (cells[2].find('a')) else "|"
        line += f"{cells[3].get_text(strip=True)} |"
        line += f"{cells[4].get_text(strip=True)} |"
        line += f"{cells[5].get_text(strip=True)} |"
        line += f"{cells[6].get_text(strip=True)} |"
        line += f"{cells[7].get_text(strip=True)} |"
        line += f"{cells[8].get_text(strip=True)} |"
        line += f"{cells[9].get_text(strip=True)} |"
        line += f"{cells[10].get_text(strip=True)} |"
        line += f"{cells[11].get_text(strip=True)} |"
        line += f"{cells[12].get_text(strip=True)} |"
        line += f"{cells[13].get_text(strip=True)} |"
        line += f"{cells[14].get_text(strip=True)} |"
        line += f"{cells[15].get_text(strip=True)} |"
        line += f"{cells[16].get_text(strip=True)} |"
        # line += f"{cells[17].get_text(strip=True)} |"
        # line += f"{cells[18].get_text(strip=True)} |"
            # line += f"{cell.get_text(strip=True)} |"
            # # Num = cells[0].get_text(strip=True)
            # # name = cells[1].get_text(strip=True)
            # # ticker = cells[2].get_text(strip=True)
            # # price = cells[3].get_text(strip=True)
            # # yield_to_maturity = cells[4].get_text(strip=True)
            # # print(f"{Num} | {ticker} | {name} | Цена: {price} | Доходность: {yield_to_maturity}")
        
        print(line)
        
        # print()

print()
