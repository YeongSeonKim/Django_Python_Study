from django.urls import path, re_path
from . import views

app_name = 'DKEA'

urlpatterns = [
    re_path(r'^(?P<c_code>C\d+)/$', views.DKEA_category_list, name='category_list'),
    re_path(r'^(?P<p_id>\d+)/$', views.DKEA_product_detail, name='product_detail'),
]
