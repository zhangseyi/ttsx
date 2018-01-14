from django.db import models


# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey('tt_user.UserInfo')
    odate = models.DateTimeField(auto_now_add=True)
    # 0待支付，1已支付待收货，2已收货待评论，3完成
    oStatus = models.IntegerField(default=0)
    ototal = models.DecimalField(max_digits=6, decimal_places=2)
    oaddress = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('tt_goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
