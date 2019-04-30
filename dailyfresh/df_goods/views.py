#coding=utf-8
from django.shortcuts import render
from models import *
from .models import GoodsInfo, TypeInfo
from df_cart.models import CartInfo
from df_user.models import UserInfo
from df_user.models import GoodsBrowser
from django.core.paginator import Paginator,Page

def index(request):
    #查出typeinfo中所有的商品类型
    typelist=TypeInfo.objects.all()
    #第一个商品类型按照新品id倒序查出四个
    type0=typelist[0].goodsinfo_set.order_by('-id')[0:4]
    # 第一个商品类型按照热度倒序查出四个
    type01=typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1=typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11=typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    #构造上下文
    # //判断是否登录

    # if 'user_id' in request.seesion:
    #     user_id = request.seesion['user_id']
    #     cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()
    cart_num = 0
    try:
        user_id = request.session['user_id']
    except:
        user_id = None

    if user_id:
        guest_cart = 1
        cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()
    context={'title':'首页','guest_cart':1,
             'type0':type0,'type01':type01,
             'type1': type1, 'type11': type11,
             'type2': type2, 'type21': type21,
             'type3': type3, 'type31': type31,
             'type4': type4, 'type41': type41,
             'type5': type5, 'type51': type51,
             'cart_num':cart_num,
             }
    return render(request, 'df_goods/index.html', context)

#tid为typeinfo的id，pindex为分页数,sort按什么排序
def list(request, tid, pindex, sort):
    #根据tid查typeinfo的id对应的数据
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    #按照id倒序从typeinfo列表中排列为最新的
    news = typeinfo.goodsinfo_set.order_by('-id')[0:4]
    # goods_list=[]
    # cart_num,guest_cart = 0,0
    # user_id = request.seesion['user_id']
    # cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()
    # if user_id:
    #     guest_cart =1
    #     cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()
    #按照id倒序查
    if sort == '1':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    #按照价格倒序查
    elif sort == '2':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('gprice')
    #按照热度倒序查
    elif sort == '3':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    #分页数
    paginator = Paginator(goods_list, 30)
    page=paginator.page(int(pindex))
    cart_num = 0
    try:
        user_id = request.session['user_id']
    except:
        user_id = None

    if user_id:
        guest_cart = 1
        cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()
    #构造上下文
    context={'title':typeinfo.ttitle,'guest_cart':1,
             'page':page,
             'paginator':paginator,
             'typeinfo':typeinfo,
             'sort':sort,
             'news':news,
             'cart_num':cart_num,}
    return render(request,'df_goods/list.html',context)

def detail(request,id):
    good_id = id
    goods=GoodsInfo.objects.get(pk=int(id))
    goods.gclick=goods.gclick+1
    goods.save()
    news=goods.gtype.goodsinfo_set.order_by('-id')[0:3]
    context={
        'title':goods.gtype.ttitle,'guest_cart':1,
        'cart_num':cart_count(request),
        'g':goods,'news':news,'id':id,
    }
    response=render(request,'df_goods/detail.html',context)

    # if 'user_id' in request.session:
    #     user_id = request.session["user_id"]
    #     try:
    #         browsed_good = GoodsBrowser.objects.get(user_id=int(user_id), good_id=int(good_id))
    #     except Exception:
    #         browsed_good = None
    #     if browsed_good:
    #         from datetime import datetime
    #         browsed_good.browser_time = datetime.now()
    #         browsed_good.save()
    #     else:
    #         GoodsBrowser.objects.create(user_id=int(user_id), good_id=int(good_id))
    #         browsed_good = GoodsBrowser.objects.filter(user_id=int(user_id))
    #         browsed_good_count = browsed_good.count()
    #         if browsed_good_count > 5:
    #             ordered_goods = browsed_good.count()
    #             for _ in ordered_goods[5:]:
    #                 _.delete()
    #     return response

    goods_ids=request.COOKIES.get('goods_ids','')
    print(goods_ids)
    goods_id='%d'%goods.id
    if goods_ids != '':
        goods_ids1=goods_ids.split(',')
        if goods_ids1.count(goods_id)>=1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id)
        if len(goods_ids1)>=6:
            del goods_ids1[5]
        goods_ids=','.join(goods_ids1)
    else:
        goods_ids=goods_id
    response.set_cookie('goods_ids',goods_ids)
    return response

def cart_count(request):
    if 'user_id' in request.session:
        return CartInfo.objects.filter(user_id=request.session['user_id']).count
        # return render(request,'df_cart/cart.html')
    else:
        return 0
def ordinary_search(request):

    from django.db.models import Q

    search_keywords = request.GET.get('q', '')
    pindex = request.GET.get('pindex', 1)
    search_status = True
    cart_num, guest_cart = 0, 0

    try:
        user_id = request.session['user_id']
    except:
        user_id = None

    if user_id:
        guest_cart = 1
        cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()

    if search_keywords:
        goods_list = GoodsInfo.objects.filter(
            Q(gtitle__icontains=search_keywords) |
            Q(gcontent__icontains=search_keywords) |
            Q(gjianjie__icontains=search_keywords)).order_by("gclick")
    else:
        search_status = False
        goods_list = GoodsInfo.objects.all().order_by("gclick")

    paginator = Paginator(goods_list, 26)
    page = paginator.page(int(pindex))

    context = {
        'title': '搜索列表',
        'search_status': search_status,
        'guest_cart': guest_cart,
        'cart_num': cart_num,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'df_goods/ordinary_search.html', context)
    # return render(request, 'search/indexes/search.html', context)