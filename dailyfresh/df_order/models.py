#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class OrderInfo(models.Model):
    oid=models.CharField(max_length=20,primary_key=True)
    #on_delete=models.CASCADE)为级联删除
    user=models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE)
    odate=models.DateTimeField(auto_now=True)
    oIsPay=models.BooleanField(default=False)
    # DecimalField
    # max_digits
    # 数中允许的最大数目的数字。请注意此电话号码必须是大于decimal_places的，如果存在的话。
    # decimal_places
    # 存储的小数位数的号码。
    ototal=models.DecimalField(max_digits=8,decimal_places=2)
    oaddress=models.CharField(max_length=150)

class OrderDetailInfo(models.Model):
    goods=models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)
    order=models.ForeignKey(OrderInfo,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    count=models.IntegerField()
    #迁移前记得添加app

