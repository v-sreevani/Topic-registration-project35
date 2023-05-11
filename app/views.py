from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def registration(request):
    TFO=TopicForm()
    WFO=WebpageForm()
    AFO=AccessRecordForm()
    d={'TFO':TFO,'WFO':WFO,'AFO':AFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        WFD=WebpageForm(request.POST)
        AFD=AccessRecordForm(request.POST)
        if TFD.is_valid() and WFD.is_valid() and AFD.is_valid():
            NSTO=TFD.save(commit=False)
            NSTO.save()
            NSWO=WFD.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()
            NSAO=AFD.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('registration successfully')
        else:
            return HttpResponse('not valid')

    return render(request,'registration.html',d)
