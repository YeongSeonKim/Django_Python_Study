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
    re_path(r'^p/modify/(?P<post_id>[0-9]+)/$', PostModifyView, name='post_modify'),
    re_path(r'^p/delete/(?P<post_id>[0-9]+)/$', PostDeleteView, name='post_delete'),  
    re_path(r'^follow/(?P<following_id>[a-zA-Z0-9-_.]*)/$', FollowView, name='follow'),
    re_path(r'^unfollow/(?P<following_id>[a-zA-Z0-9-_.]*)/$', UnfollowView, name='unfollow'),
    re_path(r'^like/(?P<post_id>[0-9]+)/$', LikePostView, name='like_post'),
    re_path(r'^unlike/(?P<post_id>[0-9]+)/$', UnlikePostView, name='unlike_post'),
    re_path(r'^collection/(?P<post_id>[0-9]+)/$', CollectionView, name='collection'),
    re_path(r'^uncollection/(?P<post_id>[0-9]+)/$', UncollectionView, name='uncollection'),
    re_path(r'^p/search/$', SearchView, name='search')
]

# MEDIA 파일 설정
# DEBUG = TRUE일 때만 작동
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DEBUG = FALSE일 때 - 배포할 경우에만 사용
# urlpatterns += re_path(r'^media/(?P<path>.\*)$', serve, {'document_root': settings.MEDIA_ROOT,})