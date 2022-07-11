from configs import URLS, data
from .commands import Help, Searchbooks, Invalidcmd
from ..api import API
from time import sleep


class Bot(API):
    def __init__(self):
        self._URL = URLS['bot_url']
        self.ERROR = None
        self._COMMANDS = [
                '/help',
                '/searchbook'
                ]

    def control(self, cmd):
        if self._isComand(cmd):
            self._execute(cmd)

    def _execute(self, cmd):
        if  '/searchbook' in cmd:
            numFiles = [str(x) for x in range(1,11)]
            if cmd[-1] in numFiles:
                maxBook = int(cmd[-1])
                query = " ".join(map(str, cmd.split()[1:-1]))
            else:
                maxBook = 5
                query = " ".join(map(str, cmd.split()[1:]))
            msms = Searchbooks(query)
            for msm in msms:
                if (msms.index(msm)+1) <= maxBook:
                    self._sendMessage(msm)
                    sleep(1)
                else:
                    break
        elif '/help' in cmd:
            self._sendMessage(Help())
        elif  '/invalid_cmd' in cmd:
            self._sendMessage(Invalidcmd())

    def _sendMessage(self, msm):
        METHOD = '/sendMessage'
        DATA = data['message']
        DATA['text'] = msm
        r = self._POST(METHOD, data=DATA)
        return r

    def _isComand(self, cmd):
        if cmd.split()[0] in self._COMMANDS:
            return True
        else:
            if cmd.startswith('/'):
                invalid_cmd = '/invalid_cmd'
                response = self._execute(invalid_cmd)
                print("Comando invalido | "+ cmd +" | ")
            else:
                print(cmd)
