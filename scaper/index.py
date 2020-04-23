from bs4 import BeautifulSoup
import requests

source = requests.get('https://webscraper.droppages.com/').text


def getHtmlText():
    return BeautifulSoup(source, 'html.parser')
