from bs4 import BeautifulSoup
from selenium import webdriver #buka chrome otomatis+ambil konten JS
# import requests
# import os

# url = 'https://id.indeed.com/jobs?'
# params = {
#     'q': 'web+developer',
#     'l': 'Banyuwangi',
#     'vjk': '892c6a95eb2f4564'
# }

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}

# res = requests.get(url, params=params, headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())

# def get_total_pages():
#     params = {
#         'q': 'web+developer',
#         'l': 'Banyuwangi',
#         'vjk': '892c6a95eb2f4564'
#     }

#     res = requests.get(url, params=params, headers=headers)

#     try:
#         os.mkdir('temp')
#     except FileExistsError:
#         pass

#     with open('temp/res.html', 'w+', encoding='utf=8') as outfile:
#         outfile.write(res.text)
#         outfile.close()

#     soup = BeautifulSoup(res.text, 'html.parser')
#     print(soup.prettify())

# if __name__ == '__main__':
#     get_total_pages()

url = "http://id.indeed.com/jobs?"
params = {
    'q': 'web+developer',
    'l': 'Banyuwangi'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'} #nyamarin scraper biar dianggep browser normal
driver = webdriver.Chrome() #manggil chromedriver+buka browser otomatis
full_url = f"{url}&q={params['q']}&l={params['l']}" #gabungin url sama param
driver.get(full_url) #browser otomatis ke halaman url
html = driver.page_source #selenium ambil html setelah js dirender

soup = BeautifulSoup(html, features='html.parser') #beautifulsoup baca html biar bisa cari elemen didalem halamanny
data = soup.find_all(name="td", attrs={'class':'resultContent'}) #cari semua sesuai name+class
for i in range(len(data)): #loop semua data
    Pekerjaan = data[i].find("h2", {'class':'jobsearch-JobInfoHeader-title css-16tttqo e1tiznh50'}) 
    Perusahan = data[i].find("div", {'class':'company-name'})
    Sallary = data[i].find("div", {'class':'salary-snippet-container'})
    if Pekerjaan and Perusahan and Sallary:
        print("Pekerjaan : " + Pekerjaan.text)
        print("Perusahaan : " + Perusahan.text)
        print("Sallary : " + Sallary.text)
        print("================================================================")

# print(Pekerjaan)
# print(Perusahan)
# print(Sallary)
print(data)

driver.quit() #nuutp browser yg dibuka selenium