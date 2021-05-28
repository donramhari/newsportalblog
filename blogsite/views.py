from django.shortcuts import render
from .models import Post



def main(request):
    return render(request, 'main.html',context = {'posts': Post.objects.all().order_by("-id")[:3]})

def postdetail(request, id):
    return render(request, 'postdetail.html',context = {'posts': Post.objects.get(id=id)})

def allposts(request):
    return render(request, 'allposts.html',context = {'posts': Post.objects.all().order_by("-id")})
