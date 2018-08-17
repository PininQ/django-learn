from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Grades, Students


# 定义视图
def index(request):
    return HttpResponse("my is a good man")


def detail(request, num, num2):
    return HttpResponse("detail-%s-%s" % (num, num2))


# 班级信息
def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades.html', {"grades": gradesList})


# 学生信息
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request, 'myApp/students.html', {"students": studentsList})


def students2(request):
    # 报异常 MultipleObjectsReturned ，如果查询没有返回结果则报 DoesNotExist
    studentsList = Students.stuObj2.get(sgender=1)
    return HttpResponse("````````````````````````")


# 显示前 5 个学生
def students3(request):
    studentsList = Students.stuObj2.all()[0:5]
    return render(request, 'myApp/students.html', {"students": studentsList})


# 分页显示学生
def stuPage(request, page=None):
    # 0-5  5-10  10-15
    #  1    2     3
    #    page*5
    page = int(page)
    studentsList = Students.stuObj2.all()[(page - 1) * 5:page * 5]
    return render(request, 'myApp/students.html', {"students": studentsList})


# 查找符合相应条件的学生信息
def studentsearch(request):
    # 查找 姓名 包含“李”的学生
    # studentsList = Students.stuObj2.filter(sname__contains="李")
    # 查找姓名包含 w 的学生，不区分大小写
    # studentsList = Students.stuObj2.filter(sname__startswith="w")
    # 查找 id 属于列表中的学生
    # studentsList = Students.stuObj2.filter(pk__in=[2, 4])
    # 查找年龄大于30的学生,大于等于 gte、小于 lt、大于等于 lte
    # studentsList = Students.stuObj2.filter(pk__gt=30)
    # 查找最后修改时间为 2018 年的学生信息
    studentsList = Students.stuObj2.filter(lastTime__year=2018)
    # 描述中带有“李四”这两个字数据是属于哪个班级的
    grade = Grades.objects.filter(students__scontent__contains='李四')
    print(grade)
    # 聚合函数：查询年龄最大的学生
    from django.db.models import Max
    maxAge = Students.stuObj2.aggregate(Max("sage"))
    print(maxAge)
    return render(request, 'myApp/students.html', {"students": studentsList})


# 某一班级的所有学生信息
def gradeInfo(request, num=None):
    # 获得对应的班级对象
    grade = Grades.objects.get(pk=num)
    # 获得班级下的所有学生对象列表
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentsList})


# 添加学生：调用 object 模型管理器
def addStudent(resquest):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("李四", 33, True, "我叫李四", grade, "2018-5-10", "2018-5-11")
    stu.save()
    return HttpResponse("方法addStudent，成功添加学生 %s" % stu.sname)


# 添加学生：调用自定义模型管理器 StudentsManager
def addStudent2(resquest):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj2.createStudent("张三", 26, True, "我叫张三", grade, "2018-3-12", "2018-4-22")
    stu.save()
    return HttpResponse("方法addStudent2，成功添加学生 %s" % stu.sname)
