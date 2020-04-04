from django.shortcuts import render,get_object_or_404
from .models import DocumentUploader,Grouping
from django.http import HttpResponseRedirect
import datetime

# Create your views here.
documents=DocumentUploader.objects.order_by("title")
grouping=Grouping()
def HomeView(request):
    #documents=DocumentUploader.objects.order_by("title")
    return render(request,'index.html',{'documents':documents})

def addGroup(request):
    group=Grouping.objects.order_by("grouptitle")
    return render(request,'addgroup.html',{'group':group})

def groupADD(request):
    if request.method=='POST':
        if request.POST['grouptitle']:
            grouping.grouptitle=request.POST['grouptitle']
            grouping.save()
            return render(request, 'index.html',{'error':'Group Successfully Added','documents':documents})

def upload(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['doc'] and request.POST['groupid']:
            document=DocumentUploader()
            
            document.title=request.POST['title']
            print (document.title)
            document.file=request.FILES['doc']
            try:
                document.group_id=Grouping.objects.get(id=request.POST['groupid']) 
                document.save()

            except :
                return render(request, 'index.html',{'error':'Invalid Group ID','documents':documents})
                
            return render(request,'index.html',{'error':'File Sucessfully uploaded','documents':documents})
        
            
        else:
            return render(request, 'index.html',{'error':'All columns are mandatory','documents':documents})
    else:
        return render(request,'index.html',{'documents':documents})
    
def read(request,group_id):
    detailread=get_object_or_404(DocumentUploader,pk=group_id)
    return render(request,'docview.html',{'document':detailread})