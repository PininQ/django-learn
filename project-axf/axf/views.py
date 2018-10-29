from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from axf.models import MainWheel, MainNav, MainMustBuy, \
    MainShop, MainShow, FoodType, Goods, CartModel, \
    OrderModel, OrderGoodsModel

from user.models import UserTicketModel
from utils.functions import get_order_random_id


def home(request):
    """
    首页视图函数
    """
    if request.method == 'GET':
        # 查询数据
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        # 组织数据
        data = {
            'title': '首页',
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainbuys': mainbuys,
            'mainshops': mainshops,
            'mainshows': mainshows,
        }
        # 携带数据渲染页面
        return render(request, 'axf/home.html', data)


def mine(request):
    """
    我的
    """
    if request.method == 'GET':
        user = request.user
        orders = OrderModel.objects.filter(user=user)
        payed, wait_pay = 0, 0
        for order in orders:
            if order.o_status == 0:
                wait_pay += 1
            if order.o_status == 1:
                payed += 1
        data = {
            "title": "我的",
            'wait_pay': wait_pay,
            'payed': payed
        }
    return render(request, 'axf/mine.html', data)


def market(request):
    """
    闪购超市
    """
    if request.method == 'GET':
        # 重定向到market_params方法所对应的路由
        return HttpResponseRedirect(reverse('axf:market_params', args=('104749', '0', '0')))


def user_market(request, typeid, cid, sid):
    """
    闪购详情
    :param request:
    :param typeid: 分类id
    :param cid: 子类id
    :param sid: 排序id
    """
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
        if user_ticket:
            user = user_ticket.user
        else:
            user = ''
        # 查询所有食品类型
        foodtypes = FoodType.objects.all()
        # 根据分类查询到对应的所有商品
        if cid == '0':
            goods = Goods.objects.filter(categoryid=typeid)
        # typeid 和 categoryid   并且是一对多的一个关系
        else:
            goods = Goods.objects.filter(categoryid=typeid, childcid=cid)

        # 重新组装全部分类的参数
        # 组装结果为[['全部分类','0'], ['酒类':13550], ['饮用水':15431]]
        foodtypes_current = foodtypes.filter(typeid=typeid).first()
        if foodtypes_current:
            childtypes = foodtypes_current.childtypenames
            childtypenames = childtypes.split('#')
            child_list = []
            for childtypename in childtypenames:
                child_type_info = childtypename.split(':')
                child_list.append(child_type_info)

        # 将商品按指定顺序排序
        if sid == '0':
            pass
        if sid == '1':
            goods = goods.order_by('productnum')
        if sid == '2':
            goods = goods.order_by('price')
        if sid == '3':
            goods = goods.order_by('-price')

        # 返回购物车信息
        if user:
            user_cart = CartModel.objects.filter(user=user)
        else:
            user_cart = ''

        # 当前选择的商品数量
        for g in goods:
            for c in user_cart:
                if c.goods.id == g.id:
                    g.num = c.c_num

        # 组织数据
        data = {
            "title": "闪送超市",
            'foodtypes': foodtypes,
            'goods': goods,
            'typeid': typeid,
            'child_list': child_list,
            'cid': cid,
            'user_cart': user_cart
        }
        # 传递数据给页面并渲染
        return render(request, 'axf/market.html', data)


def add_cart(request):
    """
    添加商品到购物车
    """
    if request.method == 'POST':
        # 获取当前用户
        user = request.user
        # 获取前端 POST 的当前商品 ID
        goods_id = request.POST.get('goods_id')
        good = Goods.objects.get(id=goods_id)
        # 定义返回 Json 格式
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        # 判断当前是系统自带的还是登录用户
        if user.id:
            if good.storenums == 0:
                data['code'] = 900
                data['msg'] = '库存不足'
                return JsonResponse(data)
            # 是登录用户就根据商品 ID 和用户获取一个购物车对象
            user_cart = CartModel.objects.filter(user=user, goods_id=goods_id).first()

            # 判断是否有购物车对象
            if user_cart:
                # 有的话商品数量 +1
                user_cart.c_num += 1
                # 保存进数据库
                user_cart.save()
                # 插入返回 json 数据
                data['c_num'] = user_cart.c_num
            else:
                # 没有购物车对象，则进行创建
                CartModel.objects.create(user=user, goods_id=goods_id)
                data['c_num'] = 1
            # 库存 -1
            good.storenums -= 1
            good.save()
            return JsonResponse(data)
        data['code'] = 403
        data['msg'] = '请先登录'
        return JsonResponse(data)


def sub_cart(request):
    """
    减少购物车用户下单商品的数量
    """
    data = {
        'code': 200,
        'msg': '请求成功'
    }
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')
        good = Goods.objects.get(id=goods_id)
        if user.id:
            # 获取用户下单对应的商品信息
            user_cart = CartModel.objects.filter(user=user, goods_id=goods_id).first()
            # 判断购物车有无此商品数据
            if user_cart:
                # 如果购物车商品只剩下最后一个
                if user_cart.c_num == 1:
                    # 删除当前商品所有信息
                    user_cart.delete()
                    # 商品数量重置为 0
                    data['c_num'] = 0
                else:
                    # 商品数量大于一个就减一
                    user_cart.c_num -= 1
                    # 保存数据到数据库
                    user_cart.save()
                    # 把减少后的商品数量添加到返回数据
                    data['c_num'] = user_cart.c_num
                # 库存 +1
                good.storenums += 1
                good.save()
                # 返回数据
                return JsonResponse(data)

        data['code'] = 403
        data['msg'] = '请先登录'
        return JsonResponse(data)


def cart(request):
    """
    购物车
    """
    if request.method == 'GET':
        # 获取用户
        user = request.user
        # 查询购物车信息
        user_carts = CartModel.objects.filter(user=user)

        data = {
            "title": "购物车",
            'user_carts': user_carts
        }
        return render(request, 'axf/cart.html', data)


def change_select_status(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart = CartModel.objects.filter(id=cart_id).first()
        if cart.is_select:
            cart.is_select = False
        else:
            cart.is_select = True
        cart.save()

        data = {
            'code': 200,
            'msg': '请求成功',
            'is_select': cart.is_select
        }
        return JsonResponse(data)


def generate_order(request):
    """
    下单
    """
    if request.method == 'GET':
        user = request.user
        # 创建订单
        o_num = get_order_random_id()
        order = OrderModel.objects.create(user=user, o_num=o_num)
        # 选择勾选的商品进行下单
        user_carts = CartModel.objects.filter(user=user, is_select=True)
        for carts in user_carts:
            # 创建商品和订单之间的关系
            OrderGoodsModel.objects.create(goods=carts.goods,
                                           order=order,
                                           goods_num=carts.c_num)
        user_carts.delete()

        return render(request, 'order/order_info.html', {'order': order})


def change_order_status(request):
    """
    修改订单状态
    """
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        OrderModel.objects.filter(id=order_id).update(o_status=1)
        data = {'code': 200, 'msg': '请求成功'}
        return JsonResponse(data)


def order_wait_pay(request):
    """
    代付款 ，o_status=0
    """
    if request.method == 'GET':
        user = request.user
        orders = OrderModel.objects.filter(user=user, o_status=0)
        data = {'orders': orders}
        return render(request, 'order/order_list_wait_pay.html', data)


def order_payed(request):
    """
    待收货 o_status=1
    """
    if request.method == 'GET':
        user = request.user
        orders = OrderModel.objects.filter(user=user, o_status=1)
        data = {'orders': orders}
        return render(request, 'order/order_list_payed.html', data)


def wait_pay_to_payed(request):
    """
    代付款订单跳转到付款页面
    """
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        order = OrderModel.objects.filter(id=order_id).first()
        data = {'orders': order}
        return render(request, 'order/order_info.html', data)


def change_cart_all_select(request):
    if request.method == 'POST':
        user = request.user
        is_select = request.POST.get('all_select')
        flag = False
        user_carts = CartModel.objects.filter(user=user)
        if is_select == '1':
            CartModel.objects.filter(user=user).update(is_select=True)
        else:
            flag = True
            CartModel.objects.filter(user=user).update(is_select=False)

        data = {
            'code': 200,
            'ids': [u.id for u in user_carts],
            'flag': flag
        }
        return JsonResponse(data)


def count_price(request):
    if request.method == 'GET':

        user = request.user
        user_carts = CartModel.objects.filter(user=user, is_select=True)
        price = 0

        for carts in user_carts:
            price += carts.goods.price * carts.c_num
        data = {
            'code': 200,
            'count_price': round(price, 3),
            'msg': '请求成功'
        }
        return JsonResponse(data)
