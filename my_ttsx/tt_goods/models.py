from django.db import models


# Create your models here.
class TypeInfo(models.Model):
    # 分类名称
    ttitle = models.CharField(max_length=20)
    # 是否删除
    isDelete = models.BooleanField(default=False)
    # 图标样式
    css = models.CharField(max_length=10)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    # 商品名称
    gtitle = models.CharField(max_length=20)
    # 图片
    gpic = models.ImageField(upload_to='goods')
    # 单价
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    # 是否删除
    isDelete = models.BooleanField(default=False)
    # 单位
    gunit = models.CharField(max_length=20, default='500g')
    # 点击量，人气
    gclick = models.IntegerField()
    # 简介
    gjianjie = models.CharField(max_length=200)
    # 库存量
    gkucun = models.IntegerField()
    # 描述
    gcontent = models.TextField()
    # 类型
    gtype = models.ForeignKey(TypeInfo)

    def __str__(self):
        return self.gtitle
