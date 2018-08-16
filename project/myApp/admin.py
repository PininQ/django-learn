from django.contrib import admin

# Register your models here.
from .models import Grades, Students


# 注册
# 自定义管理页面
# 在创建一个班级时可以直接添加两个学生
class StudentsInfo(admin.TabularInline):  # StackedInline
    model = Students
    extra = 2


# 使用装饰器完成注册
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表页属性
    # 显示字段
    list_display = ['pk', 'gname', 'ggrilnum', 'gboynum', 'isDelete']
    # 过滤字段
    list_filter = ['gname']
    # 搜索字段
    search_fields = ['gname']
    # 分页
    list_per_page = 5

    # 添加、修改页属性（下面两个属性只能使用一个，不能同时使用）
    # 属性显示的先后顺序
    # fields = ['ggrilnum', 'gboynum', 'gname', 'gdate', 'isDelete']
    # 属性的分组显示
    fieldsets = [
        ("num", {"fields": ["ggrilnum", "gboynum"]}),
        ("base", {"fields": ["gname", "gdate", "isDelete"]}),
    ]


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 布尔值显示结果修改
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    # 设置列的名称
    gender.short_description = "性别"

    def sDelete(self):
        if self.isDelete:
            return "True"
        else:
            return "False"

    sDelete.short_description = "是否删除"
    list_display = ['pk', 'sname', gender, 'sage', 'scontent', sDelete]
    list_per_page = 5

    # 设置执行动作的位置
    actions_on_top = False
    actions_on_bottom = True

# 注释这部分，改用装饰器注册
# admin.site.register(Grades, GradesAdmin)
# admin.site.register(Students, StudentsAdmin)
