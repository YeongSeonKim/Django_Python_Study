from django.urls import path, re_path
from . import views

app_name = 'DKEA'

urlpatterns = [
    re_path(r'^list/(?P<c_code>C\d+)/$', views.CategoryView, name='category_list'),
    re_path(r'^detail/(?P<p_id>\d+)/$', views.DetailView, name='product_detail'),
]
