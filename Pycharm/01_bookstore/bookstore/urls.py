from django.urls import path,re_path
from . import views

app_name = 'bookstore'

urlpatterns = [
    # path('', views.Bookstore_index, name='index'),
    re_path(r'^$', views.Bookstore_index, name='index'),
    path('<str:bookstore_code>/', views.Bookstore_detail, name='detail'),
    # re_path(r'^', views.Bookstore_detail, name='detail'),
]