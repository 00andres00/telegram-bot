from ..scrapers import Requests, Get_Soup
from ..helpers import cleanQuery, cleanData
from configs import URLS


class Get_Books:
    def __init__(self):
        self._prop = {
                'ALL_DATA':['tr', 'class', 'bookRow'],
                'INFO': [
                    ['img', 'class', 'cover', 'data-srcset'],
                    ['h3','itemprop', 'name'],
                    ['div', 'class', 'authors'],
                    ['div', 'class', 'property_year'],
                    ['div', 'class', 'property_language'],
                    ['div', 'class', 'property__file']
                    ]}
        self.Books = {}
        self._URL = URLS['Search']
        self.ERROR = False

    def searchBook(self, q):
        query = cleanQuery(q)
        s = self._URL+query
        r = Requests(s)
        r.GET()
        if r.ERROR != None:
            print(r.ERROR)
            self.ERROR = True
        else:
            self._getInfo(r.HTML)

    def _getInfo(self, HTML):
        gs = Get_Soup(HTML)
        gs.getFindAll(self._prop['ALL_DATA'])
        i=1
        for d in gs.DATA:
            gs.getFind(d, self._prop['INFO'][0])
            gs.getFind(d, self._prop['INFO'][1])
            gs.getFind(d, self._prop['INFO'][2])
            gs.getFind(d, self._prop['INFO'][3])
            gs.getFind(d, self._prop['INFO'][4])
            gs.getFind(d, self._prop['INFO'][5])
            gs.DATA2.append(d.find(self._prop['INFO'][1][0], {self._prop['INFO'][1][1]:self._prop['INFO'][1][2]}).a['href'])
            gs.DIC_DATA[i] = gs.DATA2
            gs.DATA2 = []
            i+=1
        self._cleanDatas(gs.DIC_DATA)

    def _cleanDatas(self, data):
        for i in data:
            self.Books[i] = cleanData(data[i])

    def downloadBook(self, u):
        prop = ['a', 'class', 'addDownloadedBook', 'href']
        r = Requests(u)
        r.GET()
        if r.ERROR != None:
            print(r.ERROR)
            self.ERROR = True
        else:
            gs = Get_Soup(r.HTML)
            gs.getFind(gs.soup, prop)
            print(gs.DATA2)
