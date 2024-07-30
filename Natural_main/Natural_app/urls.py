
from django.urls import path,include
from controller.items import Item_Update,Items_Views,Item_Delete,Item_Create
from controller.admin import Admin_Logout,Admin_Login
urlpatterns = [
    path('/items/',Items_Views.as_view(),name='items_views'),
    path('/items/created',Item_Create.as_view(),name='item_create'),
    path('/items/update/<int:item_id>',Item_Update.as_view(),name='item_update'),
    path('/items/delete/<int:item_id>',Item_Delete.as_view(),name='item_delete'),
    path('/admin_login/',Admin_Login.as_view(),name='admin_login'),
    path('/admin_logout/',Admin_Logout.as_view(),name='admin_logout')


]
