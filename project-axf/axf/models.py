from django.db import models
from user.models import UserModel

"""
定义数据模型
"""


# 首页栏目的父类模型，继承自框架的Model类
class Main(models.Model):
    # 图片地址
    img = models.CharField(max_length=200)
    # 栏目名称
    name = models.CharField(max_length=100)
    # 通用ID
    trackid = models.CharField(max_length=16)

    # 抽象Meta信息，供子类自定义
    class Meta:
        abstract = True


# 首页轮播：酸奶女王，优选圣女果，伊利酸奶大放价，鲜货直供－窝夫小子，鲜货直供－狼博森食品
class MainWheel(Main):
    # 轮循banner
    class Meta:
        # 定义表名
        db_table = "axf_wheel"


# 首页导航：每日必抢，每日签到，鲜货直供，鲜蜂力荐
class MainNav(Main):
    # 导航
    class Meta:
        # 定义表名
        db_table = "axf_nav"


# 首页必购：酸奶女王，鲜果女王，麻辣女王，鲜货直供－果析
class MainMustBuy(Main):
    # 必购
    class Meta:
        # 定义表名
        db_table = 'axf_mustbuy'


# 首页店铺：闪送超市，热销榜，新品尝鲜，牛奶面包，饮料酒水，优选水果，更多，鲜蜂力荐，卤味-鸭货不能停，零食轰趴，整箱购
class MainShop(Main):
    # 商店
    class Meta:
        # 定义表名
        db_table = 'axf_shop'


# 首页主要展示的商品
class MainShow(Main):
    """
    insert into axf_mainshow
    (trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,
    img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3)
     values("21782","优选水果","http://img01.bqstatic.com//upload/activity/2017031018205492.jpg@90Q.jpg",
     "103532","爱鲜蜂","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164159_996462.jpg@200w_200h_90Q",
     "103533","118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8","http://img01.bqstatic.com/upload/goods/201/611/1617/20161116173544_219028.jpg@200w_200h_90Q",
     "103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q",
     "103533","118826","爱鲜蜂·海南千禧果400-450g/盒","9.9","13.8");
    """
    # 定义一些需要的数据字段
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=100)

    # 第一件商品
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=100)
    # 价格默认0,促销价默认1
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)

    # 第二件商品
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=1)

    # 第三件商品
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=1)

    class Meta:
        # 定义表名
        db_table = "axf_mainshow"


# 闪购--左侧分类模型
class FoodType(models.Model):
    """
    --------------------------+----------+
    | id | typeid | typename     | childtypenames                                                                                                                                                                          | typesort |
    +----+--------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
    |  1 | 104749 | 热销榜       | 全部分类:0                                                                                                                                                                              |        1 |
    |  2 | 104747 | 新品尝鲜     | 全部分类:0                                                                                                                                                                              |        2 |
    |  3 | 103532 | 优选水果     | 全部分类:0#进口水果:103534#国产水果:103533                                                                                                                                              |        3 |
    |  4 | 103581 | 卤味熟食     | 全部分类:0                                                                                                                                                                              |        4 |
    |  5 | 103536 | 牛奶面包     | 全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540                                                                                                                            |        5 |
    |  6 | 103549 | 饮料酒水     | 全部分类:0#饮用水:103550#茶饮/咖啡:103554#功能饮料:103553#酒类:103555#果汁饮料:103551#碳酸饮料:103552#整箱购:104503#植物蛋白:104489#进口饮料:103556                                     |        6 |
    |  7 | 103541 | 休闲零食     | 全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545                                                                            |        7 |
    |  8 | 103557 | 方便速食     | 全部分类:0#方便面:103558#火腿肠卤蛋:103559#速冻面点:103562#下饭小菜:103560#罐头食品:103561#冲调饮品:103563                                                                              |        8 |
    |  9 | 103569 | 粮油调味     | 全部分类:0#杂粮米面油:103570#厨房调味:103571#调味酱:103572                                                                                                                              |        9 |
    | 10 | 103575 | 生活用品     | 全部分类:0#个人护理:103576#纸品:103578#日常用品:103580#家居清洁:103577                                                                                                                  |       10 |
    | 11 | 104958 | 冰激凌       | 全部分类:0                                                                                                                                                                              |       11 |
    +----+--------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
    """
    # 分类id
    typeid = models.CharField(max_length=16)
    # 分类名称
    typename = models.CharField(max_length=100)
    # 子类,字符串表示,使用#分隔不同子类
    childtypenames = models.CharField(max_length=200)
    # 展示顺序
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = "axf_foodtypes"


# 商品数据模型
class Goods(models.Model):
    """
    insert into axf_goods
    (productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,
    categoryid,childcid,childcidname,dealerid,storenums,productnum)
    values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","",
    "乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);
    """
    productid = models.CharField(max_length=16)  # 商品的id
    productimg = models.CharField(max_length=200)  # 商品的图片
    productname = models.CharField(max_length=100)  # 商品的名称
    productlongname = models.CharField(max_length=200)  # 商品的长名
    isxf = models.IntegerField(default=1)  # 精选
    pmdesc = models.CharField(max_length=100)  # 是否买一赠一
    specifics = models.CharField(max_length=100)  # 商品的规格
    price = models.FloatField(default=0)  # 商品的折后价格
    marketprice = models.FloatField(default=1)  # 商品的原价
    categoryid = models.CharField(max_length=16)  # 商品分类id
    childcid = models.CharField(max_length=16)  # 商品子分类id
    childcidname = models.CharField(max_length=100)  # 商品子分类名称
    dealerid = models.CharField(max_length=16)  # 详情页id
    storenums = models.IntegerField(default=1)  # 库存
    productnum = models.IntegerField(default=1)  # 销量排序

    class Meta:
        db_table = "axf_goods"


# 购物车
class CartModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  # 是否选择商品

    class Meta:
        db_table = 'axf_cart'


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    o_num = models.CharField(max_length=64)  # 订单号
    # 0 代表已下单未付款， 1 已付款未发货  2 已付款，已发货  3 已收货
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'axf_order'


class OrderGoodsModel(models.Model):
    goods = models.ForeignKey(Goods)  # 关联的商品
    order = models.ForeignKey(OrderModel)  # 关联的订单
    goods_num = models.IntegerField(default=1)  # 商品的个数

    class Meta:
        db_table = 'axf_order_goods'
