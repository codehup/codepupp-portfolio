from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Blog
# Create your views here.
def allposts(request):
    blogs  = Blog.objects
    return render(request, 'blog/allposts.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})

def paginate_me(request):
	post_list = Blogs.objects.all()
	paginator = paginator(post_list, 5)
	post = request.GET.get('post')
	post_list = paginator.get_post(post)
	return(request, 'blog/allposts.html', {'post_list': blogs})