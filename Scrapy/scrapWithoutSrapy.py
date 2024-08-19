import requests
from bs4 import BeautifulSoup
import timeit

file = open('quotes.txt', 'w')

def bs4Quotes(txt):
    lst = []
    s = BeautifulSoup(txt, 'lxml')
    
    for tag in s.find_all(class_ = 'text'):
        lst.append(tag.text)
        file.write(tag.text + "\n")
    return lst

def bs4(text):
    lst = []
    s = BeautifulSoup(text, 'lxml')
    
    for tag in s.find_all('a'):
        lst.append

def display(text):
    for tag in text:
        print("level 1 " + tag)
r = requests.get("https://quotes.toscrape.com/")
display(bs4Quotes(r.text))