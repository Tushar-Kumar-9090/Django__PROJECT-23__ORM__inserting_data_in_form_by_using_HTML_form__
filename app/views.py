from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

## Create your views here.

def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('<center><h1>Insertion of Topic is Done</h1></center>')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']

        TO=Topic.objects.get(topic_name=topic)
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO, name=name, url=url)[0]
        WO.save()
        return HttpResponse('<center><h1>Insertion of Webpage is Done</h1></center>')

    return render(request,'insert_webpage.html')



## here we want webpage object/instance
def insert_access_record(request):
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        date=request.POST['date']
        author=request.POST['author']

        TO=Topic.objects.get(topic_name=topic)
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO, name=name)[0]
        WO.save()
        ACO=AccessRecord.objects.get_or_create(name=WO, date=date, author=author)[0]
        ACO.save()
        return HttpResponse('<center><h1>Insertion of Access_Record is Done</h1></center>')

    return render(request,'insert_access_record.html')





# def insert_access_record(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         date=request.POST['date']
#         author=request.POST['author']

#         TO=Webpage.objects.filter(name=name)
#         TO.save()
#         WO=Webpage.objects.get_or_create(topic_name=TO, name=name)[0]
#         WO.save()
#         ACO=AccessRecord.objects.get_or_create(name=WO, date=date, author=author)[0]
#         ACO.save()
#         return HttpResponse('<center><h1>Insertion of Access_Record is Done</h1></center>')

#     return render(request,'insert_access_record.html')