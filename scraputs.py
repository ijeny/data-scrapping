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
    fungsi.write_to_file("cerita islami/cerita.doc", "isi cerita: \n")
    for p in paragraf:
        fungsi.write_to_file("cerita islami/cerita.doc", p.text)
        fungsi.write_to_file("cerita islami/cerita.doc", "=======================================================================")

def main_scrapper(url, directory, file, detail):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    articles = soup.find("div", {"id":["content"]})
    articles2 = soup.find_all("article", {"class":["post"]})

    for article in articles:
        # print("URL: ", article4.h3.a.get("href"))
        # print("Title: ", article4.h3.text, "\n")
        file_path = os.path.join(directory, file)
        detail_path = os.path.join(directory, detail)
        fungsi.write_to_file(file_path, "URL: " + article.h1.a.get("href"))
        fungsi.write_to_file(file_path, "Title: " + article.p.text + "\n")
        get_details(article.h3.a.get("href"))

system("cls")

fungsi.remove_file("cerita islami/cerita.txt")
fungsi.remove_file("cerita islami/cerita.doc")
main_scrapper("https://web.archive.org/web/20190822153936/http://cerpenmu.com/category/cerpen-islami-religi", "cerita islami", "cerita.txt", "cerita.doc")

# def main_scraper(url,directory):
# create_directory(directory) 