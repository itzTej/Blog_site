from django.shortcuts import render,HttpResponse
from blog.models import Blog
# Create your views here.
def home(request):
    return  render(request,'index.html')
def blog(request):
    blogs = Blog.objects.all()
    # Here blogs is a Query Set object
    context ={'blogs':blogs}
    return render(request,'bloghome.html',context)
def contact(request):
    return render(request,'contact.html')
def blogpost(request, slug):
    # returns a list of blog posts with given slug
    blog = Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)
def search(request):
    return render(request,'search.html')