from django.urls import path, re_path
from . import views 

app_name = 'accounts'

urlpatterns = [
    re_path(r'^register/$', views.RegisterAccountsView, name='register'),
    re_path(r'^login/$', views.LoginView, name='login'),
    re_path(r'^logout/$', views.LogoutView, name='logout'),
]
