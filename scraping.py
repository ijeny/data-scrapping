import os

def create_directory(scraping):
    if not os.path.exists(scraping):
        os.mkdir(scraping)
    
def main_scraper(url,directory):
    create_directory(directory)