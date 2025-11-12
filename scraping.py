from bs4 import BeautifulSoup
from os import system
import os
import requests
import fungsi

def get_details(url):
    # print(url) # mengecek apakah sudah ada link yang masuk atau belum
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    divEntry = soup.find("div", {'class':'read__content'})
    soup = BeautifulSoup(str(divEntry), "html.parser")
    paragraf = soup.find_all("p")
    fungsi.write_to_file("berita kompas/artikel.doc", "isi berita: \n")
    for p in paragraf:
        fungsi.write_to_file("berita kompas/artikel.doc", p.text)
    fungsi.write_to_file("berita kompas/artikel.doc", "=======================================================================")

def main_scrapper(url, directory, file, detail):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    articles = soup.find("div", {"class":["row mt3 col-offset-fluid clearfix"]})
    articles2 = articles.find("div", {"class":["col-bs10-7"]})
    articles3 = articles2.find("div", {"class":["row article__wrap__grid--flex col-offset-fluid mt2"]})
    articles4 = articles3.find_all("div", {"class":["article__box"]})

    for article in articles4:
        # print("URL: ", article4.h3.a.get("href"))
        # print("Title: ", article4.h3.text, "\n")
        file_path = os.path.join(directory, file)
        detail_path = os.path.join(directory, detail)
        fungsi.write_to_file(file_path, "URL: " + article.h3.a.get("href"))
        fungsi.write_to_file(file_path, "Title: " + article.h3.text + "\n")
        get_details(article.h3.a.get("href"))

system("cls")

fungsi.remove_file("berita kompas/artikel.txt")
fungsi.remove_file("berita kompas/artikel.doc")
main_scrapper("https://tekno.kompas.com/gadget", "berita kompas", "artikel.txt", "artikel.doc")


# def main_scraper(url,directory):
# create_directory(directory) 