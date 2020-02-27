from django.urls import path, re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve

app_name = 'instagram'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),  
    re_path(r'^(?P<user_id>[a-zA-Z0-9-_.]*)/$', PostListView, name='post_list'),
    re_path(r'^p/(?P<post_id>[0-9]+)/$', PostDetailView, name='post_detail'),  
    re_path(r'^p/upload/$', PostUploadView, name='post_upload'),  
]

# MEDIA 파일 설정
# DEBUG = TRUE일 때만 작동
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DEBUG = FALSE일 때 - 배포할 경우에만 사용
# urlpatterns += re_path(r'^media/(?P<path>.\*)$', serve, {'document_root': settings.MEDIA_ROOT,})