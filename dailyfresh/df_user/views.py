# coding=utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from hashlib import sha1
from . import user_decorator
from df_goods.models import *
from df_order.models import OrderInfo,OrderDetailInfo
from django.core.paginator import Paginator
# from ..df_goods.models import *


# Create your views here.
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    response=HttpResponse()
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    upwd2=post.get('cpwd')
    uemail=post.get('email')
    # upwd=post.get('pwd')
    if upwd != upwd2:
        return redirect('/user/register/')
    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd3=s1.hexdigest()
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail
    user.save()
    return redirect('/user/login/')

def register_exist(request):
    uname=request.GET.get('uname','aa')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})


def login(request):
    uname=request.COOKIES.get('uname', '')
    # {{alert(uname)}}
    # print(uname)
    context={'title': '用户登录', 'error_name': 0, 'error_pwd': 0, "uname": uname}
    return render(request, 'df_user/login.html')


def login_handle(request):
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0)
    users=UserInfo.objects.filter(uname=uname)
    # print(uname)
    # context={'list':users}
    # return render(request,'df_user/demo.html',context)
    if len(users)==1:
        s1=sha1()
        s1.update(upwd)
        if s1.hexdigest()==users[0].upwd:
            red = HttpResponseRedirect('/')#登录后到首页
            # red = HttpResponseRedirect('/user/info/')  登录后到用户中心
            if jizhu !=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uanme','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context={'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)
def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
    user_address=UserInfo.objects.get(id=request.session['user_id']).uaddress

    goods_ids=request.COOKIES.get('goods_ids','')
    goods_ids1=goods_ids.split(',')
    # print goods_ids
    goods_list=[]
    if len(goods_ids):
        for goods_id in goods_ids1:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    context={'title':'用户中心',
             'user_email':user_email,
             'user_name':request.session['user_name'],
             'page_name':1,
             'user_address':user_address,
             'goods_list':goods_list,
             }

    return render(request, 'df_user/user_center_info.html',context)

@user_decorator.login
def order(request,index):
    user_id = request.session['user_id']
    orders_list = OrderInfo.objects.filter(user_id=int(user_id)).order_by('-odate')
    paginator = Paginator(orders_list,2)
    page = paginator.page(int(index))
    # price = OrderDetailInfo.objects.filter()
    # dcount = int(OrderDetailInfo.count)
    # detailtotal = float(price)*float(dcount)
    # print(len(page))
    context={'title':'用户中心',
             'paginator':paginator,
             'page':page,
             'page_name':1,
             # 'detailtotal':detailtotal

             }
    return render(request,'df_user/user_center_order.html', context)

@user_decorator.login
def site(request):
    user=UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou=post.get('ushou')
        user.uaddress=post.get('uaddress')
        user.uyoubian=post.get('uyoubian')
        user.uphone=post.get('uphone')
        user.save()

    context={'title':'用户中心','user':user,'page_name':1}
    return render(request,'df_user/user_center_site.html',context)
    # return HttpResponse(user.ushou)
