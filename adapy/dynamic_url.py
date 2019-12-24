import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
class DynamicUrl:
    def __init__(self, url='http://localhost', version='v1', cache=None) :
        self._cache = cache or []
        self._baseurl = url
        self._version = version

    def __getattr__(self, name) :
        return self._(name)

    def __del__(self) :
        pass

    def _(self, name) :
        return DynamicUrl(url=self._baseurl, version=self._version, cache=self._cache+[name])

    def method(self) :
        return self._cache
    
    def create_url(self):
        url_str = '{0}/{1}'.format(self._baseurl, self._version)
        for obj in self.method() :
            url_str = '{0}/{1}'.format(str(url_str), str(obj))
        return url_str

    def get_url(self, url, params=None, json=None, timeout=30) :
        # get request
        r = requests.get(url,params=params, json=json, timeout=timeout, verify=False)
        r.raise_for_status()
        return r.json()

    def post_url(self, url, params=None, json=None, data=None, timeout=50) :
        # post request
        headers = {'Content-Type': 'application/json ;charset=utf-8'}
        r = requests.post(url,params=params, json=json, data=data, timeout=timeout, verify=False, headers=headers)
        try :
            r.raise_for_status()
        except:
            raise requests.exceptions.HTTPError('Error: {}'.format(r.json()))
        return r.json()
    
    def put_url(self, url, params=None, json=None, data=None, timeout=30) :
        # post request
        headers = {'Content-Type': 'application/json ;charset=utf-8'}
        r = requests.put(url,params=params, json=json, data=data, timeout=timeout, verify=False, headers=headers)
        try :
            r.raise_for_status()
        except :
            raise requests.exceptions.HTTPError('Error: {}'.format(r.json()))
        return r.json()
    
    def delete_url(self, url, timeout=30):
        r = requests.delete(url, timeout=timeout, verify=False)
        try :
            r.raise_for_status()
        except :
            raise requests.exceptions.HTTPError('Error: {}'.format(r.json()))
        return r.json()