from django.shortcuts import render,redirect
from .models import Data
# Create your views here.
def home(request):
    return render (request,"index.html")

def addData(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']

        obj=Data()
        obj.Name=name
        obj.Age=age
        obj.Email=email
        obj.save()

        mydata=Data.objects.all()
        return render(request,"read.html",{"datas":mydata})
    else:
        mydata=Data.objects.all()
        return render(request,"read.html",{"datas":mydata})

def updateData(request,id):
    mydata=Data.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']

        mydata.Name=name
        mydata.Age=age
        mydata.Email=email
        mydata.save()

        return redirect("addData")

    return render(request,"update.html",{'data':mydata})    

def deleteData(request,id):
    mydata=Data.objects.get(id=id)
    mydata.delete()
    return redirect("addData")