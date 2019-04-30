from django.conf.urls import url
import views
#
urlpatterns=[
    url(r'^cart/$', views.cart, name="cart"),
    url(r'add(\d+)_(\d+)/$',views.add, name="add"),
    # url(r'^demo/$',views.demo),
    url(r'^cart/edit(\d+)_(\d+)/$', views.edit, name="edit"),
    url(r'^cart/delete(\d+)/',views.delete, name="delete"),
    # url(r'^edit(\d+)_(\d+)/$',views.edit),
    # url(r'^delete(\d+)_(\d+)/$',views.delete),
 ]