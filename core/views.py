from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
import facebook

from social_django.models import UserSocialAuth

def main():
	cfg = {
		"page_id" : "324636527678327", 
		"access_token" : "EAAbZAN5ijk70BAJXyZCa2fRnVZA8yfj5ZAefQQOChlOB79zgA7meEPtrTYQAUxnZBZBrzn90R2t4TQx4sLNvRvaIISpYULMG671h6WwwH3Cl4mTXi1qrNiYkte7YZCIX5bHZAecqQGJ5MjrJTZCyufHedRZCci1KQr2KKpU4gQSMdLv2RypjuSNeFoCZAz1G0jorgzXXacJqs5tGwZDZD"
		}
		
	api = get_api(cfg)
	msg = "Hello, world!"
	status = api.put_wall_post(msg)
  
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



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
			
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def settings(request):
    user = request.user
    #main()
    try:
        linkedin_login = user.social_auth.get(provider='linkedin')
    except UserSocialAuth.DoesNotExist:
        linkedin_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None
	
    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
	
    return render(request, 'core/settings.html', {
		'linkedin_login': linkedin_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})
	
	
