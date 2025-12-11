from bs4 import BeautifulSoup
import os
import scraping
import requests

def read_data(path):
    with open(path,'rt') as file:
        for line in file:
            print(line)

read_data("hasil/hasil.txt")