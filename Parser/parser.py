from bs4 import BeautifulSoup
import requests
import csv

MAIN_URL = "https://news.ycombinator.com/"


def get_news_page(page_num=1):
    r = requests.get(MAIN_URL + "?p=" + str(page_num))

    # Превращаем сырой HTML-текст в объект BeautifulSoup, с которым удобно работать
    soup = BeautifulSoup(r.text, "html.parser")

    # Выбираем все нужные теги по css-селектору.
    # Аналогично можно сделать при помощи .find_all()
    news_titles = soup.select(".titleline > a")
    news_scores = soup.select(".score")
    news_ages = soup.select(".age")

    # Объединяем данные каждой из новостей в отельные кортежи
    news_total = zip(news_titles, news_scores, news_ages)

    return news_total


def fill_csv(news_items, csv_writer):
    # Распаковываем каждый кортеж с данными
    # Записываем эти данные в строки
    for t, s, a in news_items:
        title = t.text
        link = t.get("href")
        if link.startswith("item"):
            link = MAIN_URL + link

        points = s.text
        age = a.text

        csv_writer.writerow([title, link, points, age])


# Создаём csv-файл
with open(
    "./Parser/hacker_news.csv", mode="w", encoding="utf-8", newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link", "Points", "Age"])  # Пишем шапку таблицы

    # получаем новости постранично(пагинация)
    news = [get_news_page(i + 1) for i in range(5)]

    # Заполняем файл строками c данными о каждой новости
    for n in news:
        fill_csv(n, writer)
