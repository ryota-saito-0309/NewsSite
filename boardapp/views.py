from django.shortcuts import render
from .models import BoardModel
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect


from socket import gethostname
EMAIL_SUBJECT_PREFX = '[%s]' % gethostname()

# Create your views here.

class NewsList(ListView):
    template_name = 'list.html'
    model = BoardModel

class NewsDetail(DetailView):
    template_name = 'detail.html'
    model = BoardModel
    url = model.url
    print(url)

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')
