from bs4 import BeautifulSoup
import os
import fungsi
from selenium import webdriver # buka chrome otmatis+ambil konten JS

def main_scraper(url):
    driver = webdriver.Chrome() #manggil chromedriver+buka browser otomatis
    driver.get(url) #browser otomatis ke halaman url
    driver.set_page_load_timeout(3600)
    html = driver.page_source #selenium ambil html setelah js dirender
    soup = BeautifulSoup(html, features='html.parser') #beautifulsoup baca html biar bisa cari elemen didalem halamanny
    articles = soup.find_all("div",{'class':'latest--news mt2 clearfix'})  

    for i in range(len(articles)): #loop semua data
        berita = articles[i].find("h2", {'class':'article__list__title'}) 
        card = articles[i].find("div", {'class':'article__list clearfix'})
        if berita and card:
            print("Berita : " + berita.text)
            print("Perusahaan : " + card.text)
            print("================================================================")

    print(articles)
    driver.quit() #nutup browser yg dibuka selenium

    return html  
fungsi.create_directory('Hasil Selenium')
file_path = os.path.join('Hasil Selenium', 'kompasSelenium.txt')

html_data = main_scraper("https://tekno.kompas.com/gadget") #ngambil hasil HTML

fungsi.write_to_file(file_path, html_data) #nyimpan HTML ke file txt

print("File berhasil dibuat:", file_path)