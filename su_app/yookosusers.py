#from pymongo import MongoClient
from django.conf import settings
import json, requests

class YookosUser(object):

    def __init__(self, **attrs):

        print 'Initialising YookosUser...'

    def get_upm(self, username):
        print '>>> yoookore user get info from upm'
        url = settings.UPM_URL + username
        print url
        try:
            response  = requests.get(url)
            data      = response.json()
            print response
            return {
                    "username": data["username"],
                    "firstname": data["firstname"],
                    "lastname": data["lastname"],
                    "avatarurl": data["avatarurl"],
                    "userid": data["userid"]
                }
        except Exception, e:
            print '>>> Error', e
            return {}
#print user.get('jomski2009')
