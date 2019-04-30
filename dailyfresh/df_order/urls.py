from django.conf.urls import url
import views

app_name = 'df_order'

urlpatterns=[
    url(r'^order/$',views.order, name="order"),
    url(r'^push/$', views.order_handle, name="push"),
    url(r'^pay&(\d+)/$', views.pay, name="pay")
]