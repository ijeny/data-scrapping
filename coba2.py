import requests
import scraping
from bs4 import BeautifulSoup

# fungsi = requests.get("https://www.detik.com/")

# print(result)
# print(result.encoding)
# print(result.status_code)
# print(result.elapsed)
# print(result.url)
# print(result.history)
# print(result.headers['Content-Type'])

def main_scraper(url,directory):
    scraping.create_directory(directory) 
    source_code = requests.get(url) 
    source_text = source_code.text 
    soup = BeautifulSoup(source_text,"html.parser")
    print(soup.find_all('div',{'class':'separator'}))

main_scraper("https://ijenmoriarty.blogspot.com/", "hasil")
# print(scraping)