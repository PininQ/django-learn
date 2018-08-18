主要踩坑（随便记记）：

1. myApp\urls.py 文件（没能打印出 session 的值）

```python
# get
url(r'^get1/$', views.get1),
url(r'^get2/$', views.get2),

# post
url(r'^register/$', views.register),

# request
url(r'success/$', views.success),

# response
url(r'showresponse/$', views.showresponse),

# cookie
url(r'cookietest/$', views.cookietest),

# redirect
url(r'redirect1/$', views.redirect1),
url(r'redirect2/$', views.redirect2),

# session
url(r'main/$', views.main),
url(r'login/$', views.login),
url(r'showmain/$', views.showmain),
```

由于是一路复制粘贴，只关心视图函数，没有注意到每个匹配路径前面少了 `^`

导致 `showmain/$` 在前面找到一个匹配的路径 `main/$`

从而导致访问 `http://127.0.0.1:8000/bin/showmain/` 一直是访问 `http://127.0.0.1:8000/bin/main/`，

最后由于一直访问 `main` 函数，而没有执行到 `showmain` 函数，没能记录 session。

正确的如下：

```python
# get
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),

    # post
    url(r'^register/$', views.register),

    # request
    url(r'^success/$', views.success),

    # response
    url(r'^showresponse/$', views.showresponse),

    # cookie
    url(r'^cookietest/$', views.cookietest),

    # redirect
    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),

    # session
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$', views.showmain),
```

2. templates\login.html 文件（session 的值一直 None）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
<form action="/bin/showmain" method="post">
    <input type="text" name="username">
    <input type="submit" value="登录">
</form>
</body>
</html>
```
访问路径 `action="/bin/showmain"` 最后边少写了一个 `/` （自己一直删除 cookie 再访问一直没有效果，傻眼了）

导致获取表单的值一直为 `None`
```python
def showmain(request):
    print("========")
    # 下面两行获取的表单内容为 None
    username = request.POST.get('username')
    print("username = ", username)
    # 存储 session
    request.session['name'] = username
    return redirect('/bin/main')
```
最后在 `action="/bin/showmain"` 加上 `/` ，即可解决。


> PS：最好在 `return redirect('/bin/main')` 也加上 `/`



