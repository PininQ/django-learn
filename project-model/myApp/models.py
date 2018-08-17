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

    # 定义 Meta 类，用于设置元信息
    class Meta:
        # 定义数据表名，数据库表明默认为项目名_类名小写
        db_table = "grades"
        # 对象的默认排序字段，获取对象的列表时，获取对象的列表时使用，降序使用 ['-id']
        # PS：排序会增加数据库的开销
        ordering = ['id']


'''
1.object 是 Manager 类型的一个对象，作用是与数据库进行交互。
当定义模型类时没有指定管理器时，则 Django 为模型创建一个名为 object 的管理器

2. 自定义管理器
自定义模型管理器【使用方式：Students.stuObj.all()】
当自定义模型管理器，object 就不存在了。Django 就不再为模型类生成 object 模型管理器
stuObj = models.Manager()

3. 自定义管理器 Manager
模型管理器是 Django 的模型进行与数据库进行交互的接口，一个模型可以有多个模型管理器
作用：
1) 向管理器类中添加额外的方法。
2) 修改模型管理器返回的原始查询集，重写其方法。
'''
# 自定义管理器 Manager 类
class StudentsManager(models.Manager):
    # 修改管理器返回的原始查询集，重写 get_queryset() 方法
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    # 方法一：在自定义管理器中添加方法，创建 Student 对象
    def createStudent(self, name, age, gender, content, grade, createT, lastT, isD=False):
        stu = self.model()
        print(type(stu))
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontent = content
        stu.sgrade = grade
        stu.createTime = createT
        stu.lastTime = lastT
        stu.isDelete = isD
        return stu

class Students(models.Model):
    # 自定义模型管理器【使用方式：Students.stuObj.all()】
    # 当自定义模型管理器，object 就不存在了。Django 就不再为模型类生成 object 模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentsManager()
    sname = models.CharField(db_column="name", max_length=20)
    sgender = models.BooleanField(db_column="gender", default=False)
    sage = models.IntegerField(db_column="age")
    scontent = models.CharField(db_column="content", max_length=30)
    isDelete = models.BooleanField(db_column="isDelete", default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades")

    def __str__(self):
        return self.sname

    createTime = models.DateTimeField(auto_now_add=True)
    lastTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "students"
        ordering = ['id']

    # 方法二：定义一个类方法创建对象
    @classmethod
    def createStudent(cls, name, age, gender, content, grade, createT, lastT, isD=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontent=content, sgrade=grade, createTime=createT,
                  lastTime=lastT, isDelete=isD)
        return stu