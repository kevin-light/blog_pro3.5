from django.contrib import admin
from blog.models import *
#  admin  =  admin123

admin.site.register(User)
admin.site.register(Tag)
# admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

#自定义显示列
class ArticleAdmin(admin.ModelAdmin):
    #fields = ('title','desc','content',)    #设置显示列
    #exclude = ('title','desc','content',)    #设置相反的显示列
    list_display = ('title','desc','click_count',)  #设置admin显示列
    list_display_links = ('title','desc',)  #设置admin显示列链接
    list_editable = ('click_count',)    #设置admin显示列的可编辑

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recomment',)
        }),
    )
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh-CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(Article,ArticleAdmin)
