from django.urls import path
from . import views

app_name = 'bookmark'

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmark/<int:bookmark_pk>/', views.detail, name='detail'),
]
