# -*- coding:utf-8 -*-
# Author: xueminchao
# @Time: 2019-09-23 上午10:17

from .models import Colum



# 上下文渲染器
nav_display_columns = Colum.objects.filter(nav_display=True)


def nav_column(request):
    return {'nav_display_columns': nav_display_columns}

