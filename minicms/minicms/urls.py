"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from minicms import settings
import news.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 增加此行
    path('', news.views.index, name='index'),

    # '/$'如果没有匹配到'/'则自动添加一个'/'
    # 如果要给获取的参数起名，URL写法'index/?P<名字>表达式' 但是在视图函数接受的时候，必须使用起的名字接受
    re_path(r'^column/(?P<column_slug>[^/]+)/$', news.views.column_detail, name='column'),
    re_path(r'^news/(?P<pk>[0-9]{1,6})/(?P<article_slug>[^/]+)/$', news.views.article_detail, name='article')
    # re_path(r'^news/(?P<article_slug>[^/]+)/$',news.views.article_detail,name='article'),

]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
