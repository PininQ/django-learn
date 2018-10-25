from django.db import models


# 用户数据模型
class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)  # 用户名
    password = models.CharField(max_length=256)  # 密码
    email = models.CharField(max_length=64, unique=True)  # 邮箱
    sex = models.BooleanField(default=False)  # 性别 False 代表女
    # 头像,图片字段,上传到全局上传文件夹下的 uploads/icons/
    icon = models.ImageField(upload_to='icons')  # 头像
    is_delete = models.BooleanField(default=False)  # 是否删除

    class Meta:
        db_table = 'axf_users'


class UserTicketModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    ticket = models.CharField(max_length=256)  # 密码
    out_time = models.DateTimeField()  # 过期时间

    class Meta:
        db_table = 'axf_users_ticket'
