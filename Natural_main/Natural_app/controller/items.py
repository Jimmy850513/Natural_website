from django.shortcuts import render
from django.views.generic import TemplateView
from ..mysql_database.items import Item,Item_Status
from ..mysql_database.admin import Admin_User
# Create your views her

class Items_Views(TemplateView):
    template_name = ""
    def get(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    

class Item_Create(TemplateView):
    template_name = ""
    def get(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    
    def post(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    

class Item_Update(TemplateView):
    template_name=""
    def get(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    
    def post(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)


class Item_Delete(TemplateView):
    template_name = ""
    def get(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    
    def post(self,request,*args,**kwargs):
        template_dict = dict()
        return render(request,self.template_name,template_dict)
    