from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, CustomPasswordResetForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
	return render(request, 'user/templates/index.html', {'title':'Index'})

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')

			htmly = get_template('user/templates/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'Welcome', 'amaremek@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/templates/register.html', {'form': form, 'title':'register here'})

def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exist plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/templates/login.html', {'form':form, 'title':'log in'})


#Password change
class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'password_change.html'

#Password change done view
def custom_password_change_done(request):
       # Custom logic or functionality here
       return render(request, 'registration/password_change_done.html')


# Password reset view
class CustomPasswordResetView(PasswordResetView):
		form_class = CustomPasswordResetForm
		template_name = 'registration/password_reset.html'
		# email_template_name = 'user/templates/Email.html'
		success_url = '/password_reset/done/'
