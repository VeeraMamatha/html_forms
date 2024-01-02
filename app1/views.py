from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def topic(request):
    if request.method=='POST':
        topicname=request.POST['tn']
        a=Topic.objects.get_or_create(topic_name=topicname)[0]
        a.save()
        QLTO=Topic.objects.all()
        d={'topic':QLTO}
        return render(request,'displaytopic.html',d)



    return render(request,'topic.html')


def webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        a=Topic.objects.get(topic_name=tn)
        b=Webpage.objects.get_or_create(topic_name=a,name=na,url=ur)[0]
        b.save()
        QLWO=Webpage.objects.all()
        d1={'webpage':QLWO}
        return render(request,'displaywebpage.html',d1)


    return render(request,'webpage.html',d)
    
def accessread(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    if request.method=='POST':
            pk=request.POST['pk']
            date=request.POST['dt']
            author=request.POST['au']
            a=Webpage.objects.get(pk=pk)
            b=Accessread.objects.get_or_create(name=a,date=date,author=author)[0]
            b.save()
            QLAO=Accessread.objects.all()
            d1={'accessread':QLAO}
            return render(request,'displayaccessread.html',d1)


    return render(request,'accessread.html',d)


def select_multiple_webpages(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'webpage':QLWO}
        return render(request,'displaywebpage.html',d1)
    return render(request,'selectmultiplewebpage.html',d)


def select_multiple_accessread(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    if request.method=='POST':
        topiclist=request.POST.getlist('pk')
        QLAO=Accessread.objects.none()
        for i in topiclist:
            QLAO=QLAO|Accessread.objects.filter(pk=i)
        d1={'accessread':QLAO}
        return render(request,'displayaccessread.html',d1)
    return render(request,'selectmultipleaccessread.html',d)



def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'checkbox.html',d)
    