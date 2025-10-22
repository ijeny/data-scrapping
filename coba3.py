from bs4 import BeautifulSoup
import os
import scraping
import requests
# soup = BeautifulSoup('<html><body><div class="class1">''</div><div class="class2"></div><div class="class3"></div></body></html>')
# soup.findAll(True, {"class":["class1", "class2"]}) #mencari tag apapun (ga peduli div,p selama classnya sama)
def main_scraper(url,directory):
    scraping.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,"html.parser")
    # articles = soup.find_all("h3",{'class':'article__title article__title--medium'})
    # articles2 = soup.find_all(True,{'class':['article__box','article__title']})
    articles = soup.find_all(True,{'class':['row article__wrap__grid--flex col-offset-fluid mt2']})

    # for article in articles:
    #     print("URL : " + article.a.get("href"))
    #     print("judul : " + article.text)
    #     print()
    # for article2 in articles2:
    #     print("URL2 : " + article2.a.get("href"))
    #     print("judul2 : " + article2.text)
    #     print()
    for article in articles:
        print("URL : " + article.a.get("href"))
        print("judul : " + article.text)

main_scraper("https://tekno.kompas.com/gadget","Hasil")