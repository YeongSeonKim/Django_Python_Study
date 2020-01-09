from django.urls import path, re_path
from . import views

app_name = 'shoppingmall'

urlpatterns = [
    re_path('', views.Shoppingmall_menu_detail, name='menu_detail'),
    re_path('', views.Shoppingmall_sub_menu_detail, name='sub_menu_detail'),
]
