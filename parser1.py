import requests
from bs4 import BeautifulSoup
import csv

CSV = scores.csv
HOST = "https://mixnet.explorers.guru"
URL = "https://mixnet.explorers.guru/mixnodes"
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'}

def get_html(url):  # получаем HTML код страницы
    response = requests.get(url, headers=HEADERS)
    return response

def get_content(html):  # обрабатываем HTML код для получения нужных данных
    soup = BeautifulSoup(html, "html.parser")
    routings = soup.find_all("div", class_="css-0")#заменить на нужный класс
    scores = []


    for routing in routings:
        scores.append(
            {
                'score':routing.find('div',class_='title').get_text(strip=True), #заменить Title на нужный класс
                'link' :routing.find('div',class_='css-16vxv8a').find('a').get('href') #заменить на нужный класс
            }
        )
        return scores

def save_content(routings,path):
    with open(path,'w',newline='') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow('Routing score','Node link')
        for routing in routings:
            writer.writerow([routing['score'], [routing['link']])






