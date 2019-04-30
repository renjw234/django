#coding=utf-8
from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse,HttpResponseRedirect
from df_cart.models import *
from df_user import user_decorator
from django.http import HttpResponse
# from models import *
from .models import *
from df_goods.models import *

# @user_decorator.login
# def demo(request):
#     carts=GoodsInfo.objects.get(pk=2)
#     context={'gtitle':carts.gtitle}
#     return render(request,'df_cart/demo.html',context)
#     # return HttpResponse({'gtitle':carts.gtitle})

@user_decorator.login
def cart(request):
    uid=request.session['user_id']
    carts=CartInfo.objects.filter(user_id=uid)
    lenn=len(carts)
    context={
        'title':'购物车',
        'page_name':1,
        'carts':carts,
        'lenn':lenn,
    }
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return render(request,'df_cart/cart.html',context)
    # cartlist=CartInfor.objects.all()
    # user=cartlist.user
    # goods=cartlist.goods
    # count=cartlist.count
    # context={'user':user,'goods':goods,'count':count}
    # print (carts)
    # print(carts.gtitle)
    # print(carts.user.uname)

    # print(carts.goods.gtitle)
    # print(carts.gprice)
    # return render(request,'df_cart/cart.html',context)
    # print cartlist
    # return HttpResponse(cartlist)

@user_decorator.login
def add(request,gid,count):
    uid=request.session['user_id']
    gid, count = int(gid), int(count)
    carts=CartInfo.objects.filter(user_id=uid,goods_id=gid)
    # carts=CartInfo.objects.get(user_id=7)
    # for a in carts.user.uname:
    #     print a

    if len(carts) >= 1:
        cart=carts[0]
        cart.count=cart.count+count
    else:
        cart=CartInfo()
        cart.user_id=uid
        cart.goods_id=gid
        cart.count=count
    cart.save()
    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')
        # return redirect(reverse("df_cart:cart"))
        # return render(request,'/cart/')
# def add(request,gid,count):
#
#     #用户uid购买了gid商品，数量为count
#     uid=request.session['user_id']
#     gid = int(gid)
#     count = int(count)
#     #查询购物车是否已经有此商品，有则增加
#     carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
#     if len(carts)>=1:
#         cart=carts[0]
#         # print '*'*10
#         # print cart  -> 购物车商品数量
#         cart.count=cart.count+count
#     else:#不存在则直接加
#         cart=CartInfo()
#         cart.user_id=uid
#         cart.goods_id=gid
#         cart.count=count
#     cart.save()
#     count_s = CartInfo.objects.filter(user_id=uid).count()
#     request.session['count'] = count_s
#     #如果是ajax请求则返回json,否则转向购物车
#     if request.is_ajax():
#         # count=CartInfo.objects.filter(user_id=request.session['user_id']).count()
#
#         print '*'*10
#         print 'ajax'
#         #--------------未使用
#         return JsonResponse({'count':count_s})
#     else:
#         return redirect('/cart/')
@user_decorator.login
def edit(request,cart_id,count):
    data = {}
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        count1=cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)

@user_decorator.login
def delete(request,cart_id):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        # cart.save()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)

