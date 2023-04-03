#Import the libraries
import requests
from   bs4 import BeautifulSoup

#This function scrapes the website merriam-webster for the word of the day
def today_s_word():
    url  = 'https://www.merriam-webster.com/word-of-the-day'
    r    = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    word = soup.h2.text
    meaning = soup.find('p').get_text()
    typexx = soup.select_one('span[class^="main-attr"]').text
    pronounciation = soup.select_one('span[class^="word-syllables"]').text
    return word.title(), meaning, pronounciation, typexx