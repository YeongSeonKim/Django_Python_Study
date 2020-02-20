from django.urls import path, re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^register/$', RegisterAccountsView, name='register'),
    re_path(r'^login/$', LoginView, name='login'),
    re_path(r'^logout/$', LogoutView, name='logout'),
]