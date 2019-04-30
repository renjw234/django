from django.conf.urls import url
import views

app_name = 'df_goods'

urlpatterns=[
    url(r'^$', views.index, name="index"),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name="list"),
    url(r'^(\d+)/$', views.detail, name="detail"),
    # url(r'^cart/$', views.cart),
    url(r'^search/', views.ordinary_search, name="ordinary_search"),
]