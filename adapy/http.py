from .dynamic_url import DynamicUrl

class BaseHttpReq:
    def __init__(self, url='http://localhost', version='v1'):
        self._prod_url = url
        self._version = version
        self._dynurl = DynamicUrl(url=self._prod_url, version=self._version)

    def get(self, func='', **kwargs) :
        ''' '''
        cmd = self._dynurl
        cmd._cache = func.split('.')
        url = cmd.create_url()
        return cmd.get_url(url, **kwargs)

    def post(self, func='', **kwargs) :
        ''' '''
        cmd = self._dynurl
        cmd._cache = func.split('.')
        url = cmd.create_url()
        return cmd.post_url(url, **kwargs)
    
    def put(self, func='', **kwargs) :
        ''' '''
        cmd = self._dynurl
        cmd._cache = func.split('.')
        url = cmd.create_url()
        return cmd.put_url(url, **kwargs)
    
    def delete(self, func='') :
        ''' '''
        cmd = self._dynurl
        cmd._cache = func.split('.')
        url = cmd.create_url()
        return cmd.delete_url(url)