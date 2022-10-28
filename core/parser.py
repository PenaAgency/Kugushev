import requests
import re
from bs4 import BeautifulSoup


class YcombinatorParse:

    def __init__(self):
        self.target = 'https://news.ycombinator.com/'
        result = requests.get(self.target)
        self.soup = BeautifulSoup(result.text, 'lxml')

    def find(self):
        result = []
        items = self.soup.findAll('td', {'align': 'right', 'class': 'title'})
        for i in items:
            link = list(i.next_siblings)[2].find('a')['href']
            if not re.match('^http(s{0,1}://*)', link):
                link = '%s%s' % (self.target, link)
            title = list(i.next_siblings)[2].text
            result.append({'link': link, 'title': title})
        return result
