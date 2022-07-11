from requests import post
from json import loads


class API:
    def _POST(self, METHOD, data=None):
        data = data
        r = post(self._URL+METHOD, data=data)
        if r.ok:
            out = loads(r.text)
            return out
        self.ERROR = {'CODE': r.status_code, 'REASON:': r.reason, 'CONTENT': r.text}
        return self.ERROR

