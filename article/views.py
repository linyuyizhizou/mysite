from django.shortcuts import render,render_to_response,get_object_or_404

from django.http import HttpResponse,Http404
from .models import Article
# Create your views here.

def article_detail(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    #return HttpResponse("文章 id:%s <br> 文章内容 %s " % (article.title,article.content))
    context={}
    context['article_obj']=article
    return render_to_response("article_detail.html",context)
def article_list(request):
    articles=Article.objects.filter(is_deleted=False)
    context={}
    context['arts']=articles
    return render_to_response("article_list.html",context)