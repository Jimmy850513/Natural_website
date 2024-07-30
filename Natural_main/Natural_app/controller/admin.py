from django.shortcuts import render
from django.views.generic import TemplateView
from ..mysql_database.admin import Admin_User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
# Create your views her

class Admin_Login(TemplateView):
    template_name = ''
    def get(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    
    def post(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)

class Admin_Logout(TemplateView):
    template_name = ""
    def get(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    
    def post(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)

    