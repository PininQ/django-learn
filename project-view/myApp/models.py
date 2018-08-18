from django.db import models


class Grades(models.Model):
    # 不需要定义主键，在表生成时主键会自动添加，并且值为自动增加
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggrilnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        # return "%s-%d-%d" % (self.gname, self.ggrilnum, self.gboynum)
        return self.gname

class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=False)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades")

    def __str__(self):
        return self.sname
