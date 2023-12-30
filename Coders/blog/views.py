from django.shortcuts import render,HttpResponse
from blog.models import Blog
from blog.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def blogs(request):
    blog=Blog.objects.all()
    context={'blog':blog}
    return render(request,'blogs.html',context)
def blogpost(request, slug=None):
    if slug:
        blog=Blog.objects.filter(slug=slug).first()
        context={'blog':blog}
        return render(request,'blogpost.html',context)
        
    else:
        return render(request,'blogpost.html')
def Search(request):
    return render(request,'Search.html')

def Contact(request,method="post"):
    return render(request,method,'Contact.html')

