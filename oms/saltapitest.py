#!/usr/bin/env python
#coding=utf-8
 
import urllib2, urllib, json, re
 
class saltAPI:
    def __init__(self):
        self.__url = 'http://192.168.10.100:8000'       #salt-api监控的地址和端口如:'https://192.168.186.134:8888'
        self.__user =  'alanxsp'             #salt-api用户名
        self.__password = '852456'          #salt-api用户密码
        self.__token_id = self.salt_login()
 
    def salt_login(self):
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        encode = urllib.urlencode(params)
        obj = urllib.unquote(encode)
        headers = {'X-Auth-Token':''}
        url = self.__url + '/login'
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        try:
            token = content['return'][0]['token']
            return token
        except KeyError:
            raise KeyError
 
    def postRequest(self, obj, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token'   : self.__token_id}
        req = urllib2.Request(url, obj, headers)

        opener = urllib2.urlopen(req)

        content = json.loads(opener.read())
        return content['return']
 
    def saltCmd(self, params):
        obj = urllib.urlencode(params)
        obj, number = re.subn("arg\d", 'arg', obj)
        print "obj is %s " % obj
        res = self.postRequest(obj)
        return res

    def getminions(self):
        url = "http://192.168.10.100:8000/minions/"
        headers = {'X-Auth-Token'   : self.__token_id}
        params = {'aaa':'aaa', 'bbb':'bbbb', 'tbb':'*'}
        obj = urllib.urlencode(params)
        req = urllib2.Request(url, obj, headers)

        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        print content['return']
        return content['return']


def main(appname):
    #以下是用来测试saltAPI类的部分

    sapi = saltAPI()
    wgetcmd="wget http://192.168.10.224/yw/deploy/%s.zip -P /data/apps/%s" % (appname,appname)
    unzipcmd = "unzip -o /data/apps/%s/%s.zip -d /data/apps/%s/ " % (appname,appname,appname)
    delcmd='rm -f /data/apps/%s/%s.zip ' % (appname,appname)
    restarttomcat='/etc/init.d/newtrestart.sh'
    print wgetcmd
    print unzipcmd
    print delcmd
    allcmd = wgetcmd + "&&" +unzipcmd+ "&&" + delcmd + "&&" + restarttomcat
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'*'}
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'某台服务器的key'}
    #params = {'client':'local', 'fun':'test.echo', 'tgt':'某台服务器的key', 'arg1':'hello'}
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'testgroup', 'expr_form':'nodegroup'}
    params = {'client':'local', 'fun':'cmd.run','arg':'hostname','tgt':'PayCallBack', 'expr_form':'nodegroup'}
    #params = {'client':'local', 'fun':'status.diskusage','tgt':'testgroup', 'expr_form':'nodegroup'}
    #test = sapi.saltCmd(params)
    #print test

    sapi.getminions()

if __name__ == '__main__':
    
    main("PayCallBack")


