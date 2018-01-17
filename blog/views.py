from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


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
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form})
	
	
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form': form})