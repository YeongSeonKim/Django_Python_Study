from django.urls import path,re_path
from . import views

app_name = 'bookmark'

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^$', views.index, name='index'),
    path('<int:bookmark_pk>/', views.detail, name='detail'),
    # re_path(r'^bookmark/(?P<pk>\d+)/$', views.detail, name='detail'),
]
