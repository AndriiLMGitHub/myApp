from django.shortcuts import render
from .models import Person


# Create your views here.
def blog(request):
    blog_posts = Person.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})
