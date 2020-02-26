from django.urls import path, re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^register/$', RegisterAccountsView, name='register'),
    re_path(r'^login/$', LoginView, name='login'),
    re_path(r'^logout/$', LogoutView, name='logout'),
    re_path(r'^userinfomodify/$', UserInfoModifyView, name='userinfomodify'),
    re_path(r'^passwordmodify/$', PasswordModifyView, name='passwordmodify'),
]