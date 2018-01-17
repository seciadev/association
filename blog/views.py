from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def index(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # Generate counts of some of the main objects
	num_posts=Post.objects.all().count()
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	post1=posts[0]
	post2=posts[1]

    # Render the HTML template index.html with the data in the context variable
	return render(
        request,
        'index.html',
        context={'num_posts':num_posts, 'post1':post1, 'post2':post2 },
    )
	
def about(request):
	return render(request, 'about.html', {})
	
def news(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'news.html', {'posts': posts})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post': post, 'pk':pk})