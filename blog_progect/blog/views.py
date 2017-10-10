from django.shortcuts import render
from django.conf import settings
from blog.models import *
import logging
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger    #引入分页类

logger = logging.getLogger('blog.views')
#使用setting的logging
# import logging
# logger = logging.getLogger('blog.views')
# def index(request):
#     try:
#         file = open('sss.txt','r')
#     except Exception as e:
#         logger.error(e)

#调用settings.py的配置信息作为全局使用
def global_setting(request):
    archive_list = Article.objects.distinct_date()
    category_list = Category.objects.all()
    return locals()
    # {
    #         'archive_list':archive_list,
    #         'category_list':category_list,
    #         'SITE_NAME':settings.SITE_NAME,
    #         'SITE_DESC':settings.SITE_DESC,
    #         }

def index(request):
    try:
        # #分类信息获取（导航数据）
        # # category_list = Category.objects.all()[:1]
        # category_list = Category.objects.all()
        # #广告数据
        # ad_list = Ad.objects.all()
        # #文章归档
        # archive_list = Article.objects.distinct_date()
        # print(type(archive_list))
        #最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list,1)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)

    except Exception as e:
        logger.error(e)

    # return render(request, 'index.html', {'category_list':category_list,'article_list':article_list,})
    return render(request, 'index.html')   #locals()默认传入所有变量

def archive(request):
    try:
        # archive_list = Article.objects.distinct_date()
        # category_list = Category.objects.all()

        #先获取客户端的时间
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        # 最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 10)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.log(e)
    return render(request,'archive.html')
