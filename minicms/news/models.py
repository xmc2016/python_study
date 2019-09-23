from django.db import models
from DjangoUeditor.models import UEditorField
from django.urls import reverse
# Create your models here.
# 栏目
class Colum(models.Model):
    name = models.CharField('栏目名称',max_length=256)
    slug = models.CharField('栏目网址',max_length=256,db_index=True)
    intro = models.TextField('栏目简介',default='')
    nav_display = models.BooleanField('导航显示',default=False)
    home_display = models.BooleanField('首页显示',default=False)

    class Meta:
        verbose_name='栏目'
        verbose_name_plural=verbose_name
        ordering=['name']

    def get_absolute_url(self):
        return reverse('column',args=(self.slug,))

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    column = models.ManyToManyField(Colum,verbose_name="归属栏目")   #多对多
    title = models.CharField('标题',max_length=256)
    slug = models.CharField('网址',max_length=256,db_index=True)
    author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='作者',on_delete=models.SET_NULL)
    #content = models.TextField('内容',default='',blank=True)
    content = UEditorField('内容', width=800, height=500,
                        toolbars="full", imagePath="uploads/images/", filePath="uploads/files/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    published = models.BooleanField('正式发布',default=True)
    pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)

    def get_absolute_url(self):
#        print(reverse('article',args=(self.slug,)))
        # print(reverse('article',args=(self.pk,self.slug,)))

        return reverse('article',args=(self.pk,self.slug,))
    class Meta:
        verbose_name = '教程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


















