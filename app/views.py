from django.shortcuts import render,redirect
import datetime
from app.models import BlogData
# Create your views here.
def Home(request):
    blogData= BlogData.objects.all()
    context= {'blogData': blogData}

    return render(request,'index.html',context)

def Form(request):
    time=datetime.datetime.now()
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('Description')
        print(title)
        e=BlogData(title=title,time=time,description=description)
        e.save()
        return redirect('home')
    return render(request,'dataForm.html')



    
    