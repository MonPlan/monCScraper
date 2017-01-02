import csv
from lxml import html
import requests
import os
import codecs

class WebScraper:
    def __init__(self):
        pass

    def getAbbreviation(self, course):
        targetURL = course + '.html'
        f=codecs.open(targetURL, 'r')
        tree = html.fromstring(f.read())
        offers = tree.xpath('//p[@class="pub_highlight_value"][4]//text()')
        string = self.interpreter(offers)
        return string

    def getFaculty(self, course):
        targetURL = course + '.html'
        f=codecs.open(targetURL, 'r')
        tree = html.fromstring(f.read())
        offers = tree.xpath('//p[@class="pub_highlight_value"][6]//text()')
        string = self.interpreter(offers)
        return string


    def interpreter(self,array):
        string = ""
        for i in range(len(array)):
            newPhrase = array[i].strip('\n')
            if(newPhrase != '\n'):
                string += newPhrase
        return string

webScraper = WebScraper()

print(webScraper.getFaculty('C2000'))
