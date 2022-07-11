from bs4 import BeautifulSoup

class Get_Soup:
    def __init__(self, h):
        self.soup = BeautifulSoup(h, 'html.parser')
        self.DIC_DATA = {}
        self.DATA = []
        self.DATA2 = []

    def getTag(self, soup, prop, text=True):
        self.DATA2.append(soup.prop)

    def getFind(self, soup, prop, text=True):
        if len(prop) == 4:
            try:
                self.DATA2.append(soup.find(prop[0], {prop[1]: prop[2]})[prop[3]])
            except:
                self.DATA2.append(None)
        else:
            if text:
                try:
                    d = soup.find(prop[0], {prop[1]: prop[2]}).text
                    self.DATA2.append(d)
                except:
                    self.DATA2.append(None)
            else:
                self.DATA2.append(soup.find(prop[0], {prop[1]: prop[2]}))

    def getFindAll(self, prop):
        self.DATA = [d for d in self.soup.find_all(prop[0],{prop[1]:prop[2]})]

    def getOneandAll(self, prop):
        for d in self.soup.find_all(prop[0],{prop[1]:prop[2]}):
            t = d.select_one(prop[3])
            self.DIC_DATA[t.text] = []
            ### formato del diccionario {'id_categorie': 'url', 'name': [['ID_subcategories', 'name', 'url']]} ###
            for s in d.find_all(prop[4], {prop[5]: prop[6]}):
                sub = []
                st = s.select_one(prop[7]).text
                url = s.select_one(prop[3])['href']
                sub.append(st)
                sub.append(url)
                self.DIC_DATA[t.text].append(sub)

    def getDatas(self, prop, info):
        self.getFindAll(prop['ALL_DATA'])
        for d in self.DATA:
            self.getFind(d, prop['TITLE'])
            self.getFind(d, prop['PRE_PRICE'])
            self.getFind(d, prop['PRICE'])
            self.getFind(d, prop['FREE_SHIP'])
            self.getFind(d, prop['URL'], href=True)
            self.DIC_DATA[i] = self.DATA2
            self.DATA2 = []

