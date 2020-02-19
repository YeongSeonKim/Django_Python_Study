from django.urls import path, re_path
from . import views 

app_name = 'instagram'

urlpatterns = [
    re_path(r'^$', views.MainView, name='main'),  
    re_path(r'^post_create/$', views.PostCreateView, name='post_create'),  
    re_path(r'^(?P<user_id>[a-zA-Z0-9-_.]*)/$', views.PostListView, name='my_post_list'),
    re_path(r'^post_detail/$', views.PostDetailView, name='each_post_detail'),  
]
