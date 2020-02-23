from django.urls import path, re_path
from .splitviews import *

app_name = 'instagram'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),  
    re_path(r'^post_create/$', PostCreateView, name='post_create'),  
    re_path(r'^(?P<user_id>[a-zA-Z0-9-_.]*)/$', PostListView, name='post_list'),
    re_path(r'^post_detail/$', PostDetailView, name='each_post_detail'),  
]
