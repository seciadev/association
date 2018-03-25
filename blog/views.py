from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
import facebook

def home(request):
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
	
def login(request):
	return render(request, 'login.html', {})
	
def news(request):
	draftposts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'news.html', {'posts': posts, 'draftposts':draftposts})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post': post, 'pk':pk})
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
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
			if (post.published_date==None):
				#do nothing
				a=1
			else:
				post.published_date= timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form': form})
	
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    cfg = {
        "page_id"      : "324636527678327",  # Step 1
        "access_token" : "EAAbZAN5ijk70BAAZCzCVpyfUWQuzYIUllurRSexhx66bnzgVMuZBMWrXZC1sh2tWttw2sCdTFriPDw9qYmpSbArRyFaELb6OY0ZBBjobjWEmUtsvpkVLt08mwyXGU4kbOPuGfBJvBI7J1giYNWKAKQn2MgKjbgJcZD"   # Step 3
        }

    api = get_api(cfg)
    
    msg = "http://www.corriere.it/tecnologia/18_marzo_21/scandalo-facebook-zuckerberg-sono-responsabile-quanto-accaduto-208d46aa-2d40-11e8-af9b-02aca5d1ad11.shtml"
    #attachment = {
    #    'name': 'Alinnova',
	#	'link': 'https://www.alinnova.eu',
	#	'caption': post.title,
	#	'description': post.text,
	#	'picture': ''
	#	}
    
    status = api.put_object(
        parent_object="me",
        connection_name="feed",
        message="This is a great website. Everyone should visit it.",
        link="https://www.alinnova.eu")
    #status = api.put_object(parent_object='me', connection_name='feed', message=msg)	
	#status = api.put_wall_post(msg)
	
    post.publish()
    return redirect('post_detail', pk=pk)
	
	
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph