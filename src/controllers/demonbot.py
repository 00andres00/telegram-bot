from ..api import API
from ..helpers import read, write
from .bot import Bot
from .commands import Help, Searchbooks
from configs import URLS, fileLastUpdate
from .lastUpdate import lastUpdateID

class DemonBot(API):
    def __init__(self):
        self._URL = URLS['bot_url']
        self.ERROR = None
        self._METHOD = '/getUpdates'
        self._LAST = lastUpdateID
        self._bot = Bot()

    def _lastUpdate(self, c):
        wc = 'lastUpdateID = '+str(c)
        write(fileLastUpdate, wc)

    def check(self):
        while True:
            r = self._POST(self._METHOD, data=self._LAST)
            if self.ERROR != None:
                print(self.ERROR)
            else:
                for i in r['result']:
                    if self._LAST['offset'] < i['update_id']:
                        self._LAST['offset'] = i['update_id']
                        self._lastUpdate(self._LAST)
                        if 'message' in i and 'text' in i['message']:
                            cmd = i['message']['text']
                            self._bot.control(cmd)

