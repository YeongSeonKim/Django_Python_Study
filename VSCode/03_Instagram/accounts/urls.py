from django.urls import path, re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve

app_name = 'accounts'

urlpatterns = [
    re_path(r'^register/$', RegisterAccountsView, name='register'),
    re_path(r'^login/$', LoginView, name='login'),
    re_path(r'^logout/$', LogoutView, name='logout'),
    re_path(r'^userinfomodify/$', UserInfoModifyView, name='userinfomodify'),
    re_path(r'^passwordmodify/$', PasswordModifyView, name='passwordmodify'),
]

# MEDIA 파일 설정
# DEBUG = TRUE일 때만 작동
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DEBUG = FALSE일 때 - 배포할 경우에만 사용
# urlpatterns += re_path(r'^media/(?P<path>.\*)$', serve, {'document_root': settings.MEDIA_ROOT,})