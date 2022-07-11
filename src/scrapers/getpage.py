from requests import get

class Requests:
    def __init__(self, url):
        self._URL = url
        self.HTML = None
        self.ERROR = None

    def GET(self):
        r = get(self._URL)#, verify=False)
        if r.ok:
            self.HTML = r.text
        else:
            self.ERROR = {
                    'Status_code': r.status_code,
                    'Reason': r.reason,
                    'Url': r.url
                    }


