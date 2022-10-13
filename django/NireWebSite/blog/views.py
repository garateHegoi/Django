from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.

def post_list(request):
    postak = Post.objects.all()
    p = 0
    for x in postak:
        p += x.prezioa
    return render(request, 'blog/post_list.html', {'postak': postak, 'p': p})


def add(request):
    return render(request, 'blog/add.html')


def addrecord(request):
    x = request.POST['author']
    y = request.POST['title']
    xy = request.POST['prezioa']
    z = request.POST['text']
    post = Post(author=x, title=y, prezioa=xy, text=z)
    post.save()
    return HttpResponseRedirect(reverse('blog/'))


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('blog/'))


def update(request, id):
    postak = Post.objects.get(id=id)
    template = loader.get_template('blog/update.html')
    context = {'postak': postak}
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    author = request.POST['author']
    title = request.POST['title']
    prezioa = request.POST['prezioa']
    text = request.POST['text']
    post = Post.objects.get(id=id)
    post.author = author
    post.title = title
    post.prezioa = prezioa
    post.text = text
    post.save()
    return HttpResponseRedirect(reverse('blog/'))
