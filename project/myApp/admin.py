from django.contrib import admin

# Register your models here.
from .models import Grades, Students


# 注册
# 自定义管理页面
class StudentsInfo(admin.TabularInline): # StackedInline
    model = Students
    extra = 2


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


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sname', 'sgender', 'sage', 'scontent', 'isDelete']
    list_per_page = 5


admin.site.register(Grades, GradesAdmin)
admin.site.register(Students, StudentsAdmin)
