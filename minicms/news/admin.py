from django.contrib import admin
from .models import Colum,Article

@admin.register(Colum)
class ColumAdmin(admin.ModelAdmin):
    list_display = ('name','slug','intro',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','pub_date','update_time')



