from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.core.urlresolvers import reverse
from article.models import Comment, Article
from user.models import User
from django.core import serializers
import re
import json

# Create your views here.
article_code = {
    'not_login': 100,
    'not_authority': 101,
    'article_not_exist': 102,
    'article_exist': 103,
    'comment_not_exist': 104,
    'comment_exist': 105,

    'article_show_success': 110,
    'article_create_success': 111,
    'article_delete_success': 112,
    'article_modify_success': 113,
    'article_liked_success': 114,
    'article_user_show_success': 115,
    'comment_user_show_success': 116

}


def test(request):
    return render(request, "test.html", {"text": "hello world"})





# need username, title, author
def article_operation(request):
    # check up whether user has login
    username = request.COOKIES['username']
    # put into FrontEnd or BackEnd ???
    if not username:
        return HttpResponse(json.dumps({'mode': article_code['not_login']}))
    data = eval(request.POST.get('data', None))
    if data is None:
        pass
    '''
    article/(\d+)
    通过id传递文章
    session的名称可为article+str(id)
    '''
    # use id is also ok, it may faster than using title+author, get from article/(\d+)
    title = data['title']
    author = data['author']
    article = Article.objects.get(title=title, author=author)

    # show an article
    def article_show():
        if article:
            return HttpResponse(json.dumps({'article': serializers.serialize("json", [article]),
                                            'comment': serializers.serialize("json", article.comments.all()),
                                            'mode': article_code['article_show_success']}))
        return HttpResponse(json.dumps({'mode': article_code['article_not_exist']}))

    # create an article
    def article_create():
        if not article:
            text = data['text']
            Article.objects.create(title=title, author=author, text=text)
            return HttpResponse(json.dumps({'mode': article_code['article_create_success']}))
        return HttpResponse(json.dumps({'mode': article_code['article_exist']}))

    # delete an article
    def article_delete():
        # judge in BackEnd or FrontEnd ???
        if author != username:
            return HttpResponse(json.dumps({'mode': article_code['not_authority']}))
        if article:
            article.delete()
            return HttpResponse(json.dumps({'mode': article_code['article_delete_success']}))
        return HttpResponse(json.dumps({'mode': article_code['article_not_exist']}))

    # modify an article
    def article_modify():
        # judge in BackEnd or FrontEnd ???
        if author != username:
            return HttpResponse(json.dumps({'mode': article_code['not_authority']}))
        text = data['text']
        if article:
            article.update(text=text)
            return HttpResponse(json.dumps({'mode': article_code['article_modify_success']}))
        return HttpResponse(json.dumps({'mode': article_code['article_not_exist']}))

    # press the "liked" button in an article
    def article_liked():
        if article:
            article.update(liked=article.liked + 1)
            return HttpResponse(json.dumps({'mode': article_code['article_liked_success']}))
        return HttpResponse(json.dumps({'mode': article_code['article_not_exist']}))

    mode = data['mode']
    mode = {
        1: article_show(),
        2: article_create(),
        3: article_delete(),
        4: article_modify(),
        5: article_liked()
    }
    article.update(views=article.views + 1)
    '''
        # check up whether user has visited the article
        cookie_article = 'article'+str(article.id)
        if not request.COOKIES[cookie_article]:
            article.update(views=article.views + 1)
            response.set_cookie('cookie_article', 1, max_age=3600)
    '''


# need username & author is equal to username
def comment_operation(request):
    # check up whether user has login
    username = request.COOKIES['username']
    if not username:
        return HttpResponse(json.dumps({'mode': article_code['not_login']}))

    data = eval(request.POST.get('data', None))
    author = data['author']
    # judge in BackEnd or FrontEnd ???
    if author != username:
        return HttpResponse(json.dumps({'mode': article_code['not_authority']}))
    content = data['content']
    comment = Comment.objects.get(author=author, content=content)

    def comment_create():
        if not comment:
            Comment.objects.create(author=author, comment=comment)
        return HttpResponse(json.dumps({'mode': article_code['comment_exist']}))

    def comment_delete():
        if comment:
            comment.delete()
        return HttpResponse(json.dumps({'mode': article_code['comment_not_exist']}))

    mode = data['mode']
    mode = {
        1: comment_create(),
        2: comment_delete(),
    }


# need username . author is equal to username
# show all articles created by a specific user
def user_operation(request):
    # check up whether user has login
    username = request.COOKIES['username']
    if not username:
        return HttpResponse(json.dumps({'mode': article_code['not_login']}))

    def user_show_article():
        article = Article.objects.get(author=username)
        return HttpResponse(json.dumps({'mode': article_code['article_user_show_success'],
                                    'article': serializers.serialize("json", [article])}))
        # 只传article的一部分，如id,title,content的前一部分，(liked,visit)
    def user_show_comment():
        comment = Comment.objects.get(author=username)
        return HttpResponse(json.dumps({'mode': article_code['comment_user_show_success'],
                                        'comment': serializers.serialize("json", [comment])}))

    data = eval(request.POST.get('data', None))
    mode = data['mode']
    mode = {
        1: user_show_article(),
        2: user_show_comment()
    }


'''
1.
.objects.get :
.all QuerySet, can use iterator
.get List : add []

2. In BackEnd :
    get messages : eval() : json(dict) -> str
    send messages : json.dumps() : json(dict) -> str
'''
