from django.shortcuts import render,HttpResponse
from blog.models import Blog

# Create your views here.
def home(request):
    return render(request,'home.html')
def blogs(request):
    blog=Blog.objects.all()
    context={'blog':blog}
    return render(request,'blogs.html',context)
def blogpost(request, slug=None):
    if slug:
        return HttpResponse(f"You are viewing {slug}")
    else:
        return render(request,'blogpost.html')
def Search(request):
    return render(request,'Search.html')

def Contact(request):
    return render(request,'Contact.html')

