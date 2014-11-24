"""Core class for Simple-Crunchbase"""
import datetime
import argparse
import requests
from collections import OrderedDict

class CrunchBaseType(object):
    def __init__(self, user_key, object_name):
        self.name = object_name.lower()
        self.user_key = user_key
        self.base_url = ('http://api.crunchbase.com/v/2/{object_name}/'.format(object_name=self.name))

    def get(self, *args, **kwargs):
        if kwargs.get('permalink'):
            self.base_url += kwargs.get('permalink')

        result = self._call_crunchbase('GET', self.base_url, kwargs)
        if result.status_code == 200:
            return result.json(object_pairs_hook=OrderedDict)
        raise CrunchBaseError(result)

    def _call_crunchbase(self, method, url, kwargs):
        kwargs.update({'user_key':self.user_key})
        return requests.request(method, url, params=kwargs)

class CrunchBase(object):
    def __init__(self, **kwargs):
        if 'user_key' in kwargs:
            self.user_key = kwargs['user_key']

    def __getattr__(self, name):
        return CrunchBaseType(self.user_key, name)

class CrunchBaseError(Exception):
    def __call__(self, *args):
        return self.__class__(*(self.args + args))