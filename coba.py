# import os

# def create_directory(Scrapping):
#     if not os.path.exists(Scrapping):
#         os.mkdir(Scrapping)

# create_directory("Scrapping")

# def create_new_file(path,data):
#     with open(path,'a') as file:
#         file.write(data +'\n')

# create_new_file('Scrapping/test.txt','pppp')

# def clear_file(path):
#     f = open(path,'a')
#     f.close()

# clear_file("Scrapping/test.txt")

# def create_new_file(path):
#     f = open(path,'w')
#     f.write("")
#     f.close()

# def write_to_file(path,data):
#     with open(path,'a') as file:
#         file.write(data +'\n')

# def read_data(path):
#     with open(path,'rt') as file:
#         for line in file:
#             print(line)

# create_new_file("scrapping/file.txt")
# write_to_file("scrapping/file.txt","haloo\n")
# write_to_file("scrapping/file.txt","ayo roblok\n")
# read_data("scrapping/file.txt")

# def does_file_exist(path):
#     return os.path.exists(path)

# def remove_file(path):
#     if does_file_exist(path):
#         os.remove(path)
#         print("berhasil dihapus")
#     else:
#         print("file tidak ditemukan")

# remove_file("Scrapping/test.txt")

from bs4 import BeautifulSoup

html1 = "<p>This is Div</p>"
soup = BeautifulSoup(html1,"html.parser")

print(soup.p.text)

html = "<div>ini adalah dokumen div</div><p>ini adalah paragraf halaman luar</p>"

soup = BeautifulSoup(html,"html.parser")

print(soup.p.text)

html = """<div>ini div</div><p>ini paragraf</p><div>p</div>"""

soup = BeautifulSoup(html,"html.parser")

print(soup.findAll("div")[1])

html = """
    <div>div 1</div>
    <p>p 1</p>
    <div class='bold'>ini div bold</div>
"""
soup = BeautifulSoup(html,"html.parser")

# print(soup.findAll("div",{'class':'bold'}))

print(soup.findAll("P",{'id':'para'}))

html = """
    <div id="d1" class="wide">
        <p id='p1'>ini paragraf</p>
        <img src=""/>
        <a id="a1"></a>
    </div>
    <div id="d2" class="small">
        <p id='p2'>ini paragraf 2</p>
        <img src=""/>
        <a id="a2"></a>
    <.div>
"""

soup = BeautifulSoup(html,"html.parser")

print(soup.findAll('div',{'id':'d2'})[0].p)

html = """
    <div id="d1" class="wide">
        <p id='p1'>ini paragraf</p>
        <div><p>OK</p></div>
        <img src=""/>
        <a id="a1"></a>
    </div>
    <div id="d1" class="small">
        <p id='p1'>ini paragraf 2</p>
        <div><p>KO</p></div>
        <img src=""/>
        <a id="a1"></a>
    <.div>
"""

soup = BeautifulSoup(html,"html.parser")

print(soup.findAll('div',{'id':'d1','class':'small'})[0].div.p.text)

html = """
    <div>div1</div>
    <div>div2</div>
    <div>div3</div>
    <div>div4</div>
    <div>div5</div>
    <div>div6</div>
    <div>div7</div>
    <div>div8</div>
    <div>div9</div>
    <div>div10</div>
"""
soup = BeautifulSoup(html,"html.parser")

# print([soup.findAll('div')[div].text for div in[1,3,5,7,9]])
# print(soup.findAll('div')[3].text)
for index, div in enumerate(soup.findAll("div")):
    if (index + 1) % 2 == 0:
        print(div)