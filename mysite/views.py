from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime
# Create your views here.
#取得所有紀錄
def homepage(request): #request接收參數
    posts = Post.objects.all() #获取所有 Post
    now = datetime.now()

    return render(request, "index.html", locals())
    #返回当前函数的所有局部變數以字典的形式。包含 posts 和 now 
    
    '''
    post_list = list()
    for count, post in enumerate(posts):
        post_list.append("No.{}: ".format(str(count) + str(post) + "<hr>")) #標題
        post_list.append("<small>" + str(post.body) + "<small><br><br>") #內容
    return HttpResponse(post_list)
    '''

def showpost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html' ,locals())
    except:
        return redirect('/')