from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import appmodel,Article
from django.contrib import messages
from .filter import Orderfilter
def homepage(request):
    return render(request,"html/home.html")

def signup(request):
    
    if request.method == "POST":
        user=request.POST["username"]
        fname=request.POST["fname"]
        last=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        paas2=request.POST["pass2"]

        myuser=User.objects.create_user(user,email,pass1)
        myuser.first_name=fname
        myuser.last_name=last

        myuser.save()

        messages.success(request,"your account is successfully created!")

        return redirect("signin")
    
    return render(request,"html/register.html")

def signin(request):
    if request.user.is_authenticated:
         return redirect("main")
    
    if request.method == "POST":
            useranme=request.POST["username"]
            pass1=request.POST["pass1"]
        
            user=authenticate(username=useranme,password=pass1)
             
            if user is not None:
               login(request, user)
               fname=user.first_name
               return redirect('main')
            
            else:
                messages.error(request,"something error 'user' or 'password'")
                return render(request,"html/login.html")
    return render(request,"html/login.html")

def logoutview (request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect("home")



def home (request):
    if request.user.is_authenticated:
        name=request.user.username
        return render(request,"html/arasu.html",{"name":name})
    else:
        return redirect('home')


def venderadd(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":
            name=request.POST["vendar"]
            fathername=request.POST["father"]
            number=request.POST["mobile"]
            address=request.POST["area"]
            join=request.POST["join"]

            form=appmodel.objects.create(name=name,fathername=fathername,number=number,address=address,join=join)
            form.save()
            messages.success(request,"vendor successfully added")

            return redirect("details")
        return render(request,"html/form.html")
    else:
        return redirect("home")


    

def venderdetails(request):
    if request.user.is_authenticated:
        details=appmodel.objects.all()
        return render(request,"html/main.html",{"data":details})
    else:
        return redirect("home")
    
def update(request,id):
    if request.user.is_authenticated:
        name=appmodel.objects.get(id=id)
        if request.method == "POST":
            vender=request.POST["vendar"]
            father=request.POST["father"]
            number=request.POST["mobile"]
            address=request.POST["area"]
            join=request.POST["join"]

            name.name=vender
            name.fathername=father
            name.number=number
            name.address=address
            name.join=join
            name.save()
            messages.success(request,"successfully changed")
        
            return redirect('details')
        return render(request,"html/sample.html",{"name":name})
    else:
        return redirect("home")

def updatebutton(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            getid=request.POST["getid"]
            return render(request,"html/update.html",{"id":getid})
        return render(request,"html/update.html")
    else:
        return redirect("home")



def deletebutton(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            delid=request.POST['getid']
            return render(request,'html/delete.html',{"delid":delid})
        return render(request,"html/delete.html")
    else:
        return redirect("home")


def deletefile(request,id):
    if request.user.is_authenticated:
        data=appmodel.objects.get(id=id)
        data.delete()
        messages.success(request,"successfully deleted")

        return redirect('details')
    else:
        return redirect("home")

def getbillid(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            getid=request.POST["getid"]
            return render(request,"html/billid.html",{"id":getid})
        return render(request,"html/billid.html")
    else:
        return redirect("home")

def billform(request,id):
    if request.user.is_authenticated:
        details=appmodel.objects.get(id=id)
        details.save()
        
        if request.method == "POST":
            id=request.POST["id"]
            name=request.POST["name"]
            Date=request.POST["date"]
            litre=int(request.POST["litre"])
            rate=litre*40
            add=Article(id=None,date=Date,name=name,litre=litre,rate=rate,vendor=details)
            add.save()
            return redirect("billreport")

        return render(request,"html/billform.html",{"data":details})
    else:
        return redirect('home')

def billreport(request):
    if request.user.is_authenticated:

        allbill=Article.objects.all()
        filter=Orderfilter(request.GET, queryset=allbill)
        allbill=filter.qs
        return render(request,"html/billreport.html",{"data":allbill,"filter":filter})
    else:
        return redirect('home')
def billserch(request):
    if request.user.is_authenticated:
        if request.method == "POST":
           getid=request.POST["getid"]
           return render(request,"html/filter.html",{"data":getid})
        
        return render(request,"html/filter.html")
    else:
        return redirect('home')

def billreportfilter(request,id):
    if request.user.is_authenticated:
        filter=Article.objects.filter(vendor=id)
        return render(request,"html/filter.html",{"details":filter})

    else:
        return redirect('home')
    
def billview(request,id):
    if request.user.is_authenticated:
        data=Article.objects.get(id=id)
        return render(request,"html/billview.html",{"data":data})