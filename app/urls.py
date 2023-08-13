from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.homepage , name="home"),
    path("signup",views.signup, name="signup"),
    path("signin",views.signin, name="signin"),
    path("logout",views.logoutview,name="logout"),
    path("home",views.home, name="main"),
    path("addvender",views.venderadd, name="vender"),
    path("venderdetails",views.venderdetails,name="details"),
    path("updatebutton",views.updatebutton,name="upbutton"),
    path("update/<int:id>",views.update,name="update"),
    path("del/<int:id>",views.deletefile,name="delete"),
    path("delete",views.deletebutton,name="delbtn"),
    path("bill/<int:id>",views.billform,name="billform"),
    path("billid",views.getbillid,name="billid"),
    path("billreport",views.billreport,name="billreport"),
    path("vendorwise",views.billserch,name="vendorwise"),
    path("vendorbill/<int:id>",views.billreportfilter,name="vendorbill"),
    path("billview/<int:id>",views.billview,name="billview"),
]

    