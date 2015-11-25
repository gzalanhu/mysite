from django.shortcuts import render
from django.shortcuts import render
import sys
import os,re
import datetime,commands
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.utils import simplejson
import json as simplejson
from models import Progame
from saltapitest import *

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    print "now is %s" % now
    return render_to_response('index.html', {'Res': 'res'})
def dash(request):
    now = datetime.datetime.now()
    print "now is %s" % now
    return render_to_response('dashborad.html', {'Res': 'res'})

def deploy(request):
    now = datetime.datetime.now()
    print "now is %s" % now
    Res={}
    pronamelist={}
    Progames1 = Progame.objects.all()
    for x in Progames1:
        if pronamelist.has_key(x.ProName):
            pronamelist[x.ProName] = []
        else:
            pronamelist[x.ProName] = []
    print "12313 pronamelist  %s "  % pronamelist
    Progames = Progame.objects.all()
    res = []
    Apps={}


    for t in Progames:
        Apps['id']=t.id
        Apps['appname']=t.AppName
        Apps['proname']=t.ProName
        Apps['domain']=t.Domain
        Apps['apptype']=t.Apptype
        pronamelist[t.ProName].append(Apps)
        Apps={}
        print pronamelist

    print "pronamelist is %s" % pronamelist
    for key,value in pronamelist.items():
         Res['proname']=key
         Res['apps']=value
         print Res
         res.append(Res)
         Res = {}

    #print res
    print "res is %s" % res
    #res=[{'proname':'gamesdk','apps':[{'appname':'admin','proname':'gamesdk','domain':'mis.91cw.cn'},{'appname':'channel','proname':'gamesdk','domain':'channel.91cw.cn'}]},{'proname':'singlegame','apps':[{'appname':'singleadmin','proname':'singlegame','domain':'mis.single.cn'}]}]
    return render_to_response('deploy.html', {'Res': res})

def deploystart(request):

    if request.method == 'POST':
        appname = request.REQUEST.get('appname')
        proname = request.REQUEST.get('proname')
        domain = request.REQUEST.get('domain')
    print appname,proname,domain
    Results="b"
    sapi = saltAPI()
    os.environ["LANG"] ="zh_CN.UTF-8"
    wgetcmd="wget http://192.168.10.224/yw/deploy/%s.zip -P /data/apps/%s" % (appname,appname)
    unzipcmd = "unzip -o /data/apps/%s/%s.zip -d /data/apps/%s/ " % (appname,appname,appname)
    delcmd='rm -f /data/apps/%s/%s.zip ' % (appname,appname)
    restarttomcat='/etc/init.d/newtrestart.sh'
    groupname=appname
    print wgetcmd
    print unzipcmd
    print delcmd
    print sapi
   # allcmd = wgetcmd + "&&" +unzipcmd+ "&&" + delcmd + "&&" + restarttomcat
    allcmd = "export LC_ALL='zh_CN.UTF-8';" + wgetcmd + "&&" +unzipcmd+ "&&" + delcmd + "&&" + restarttomcat
    print allcmd
    params = {'client':'local', 'fun':'cmd.run','arg':allcmd,'tgt':groupname, 'expr_form':'nodegroup'}
    sapires = sapi.saltCmd(params)
    print "sapires is %s " % sapires
    return HttpResponse(simplejson.dumps(Results,ensure_ascii = False))

def appsetting(request):
    now = datetime.datetime.now()
    print "now is %s" % now
    Progames = Progame.objects.all()
    re = []
    for t in Progames:
        Re = {}
        project = []
        Re['id'] = t.id
        Re['AppName'] = t.AppName
        Re['ProName'] = t.ProName
        Re['Domain'] = t.Domain
        Re['AppType'] = t.Apptype
        print "Re is %s" % Re
        re.append(Re)
    return render_to_response('appsetting.html', {'Res': re})


def addapp(request):
    now = datetime.datetime.now()

    if request.method == 'POST':

        INFO = {}
        Tuple = ('appname','progame','domain','apptype')
        for i in Tuple:
            INFO[i] = request.POST.get(i)
            print INFO[i]
        DBDA = Progame(AppName=INFO['appname'],ProName=INFO['progame'],Domain=INFO['domain'],Apptype=INFO['apptype'])
        print "DBDA is %s" % DBDA
    print DBDA
    DBDA.save()
    Results = {'a':'ttttb'}
    return HttpResponse(simplejson.dumps(Results,ensure_ascii = False))


def assets(request):
    now = datetime.datetime.now()
    print "now is %s" % now
    return render_to_response('assets.html', {'Res': 'res'})


#def test(request):
#    now = datetime.datetime.now()
#    print "now is %s" % now
#    return render_to_response('test.html', {'Res': now})