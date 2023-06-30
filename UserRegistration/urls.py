from django.contrib import admin
from django.urls import path, include
from Users import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [

	path('admin/', admin.site.urls),
	path('', include('Users.urls')),
	path('login/', auth_views.LoginView, name ='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name ='user/templates/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),

	# Password reset URLs
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	path('password/change/', MyPasswordChangeView.as_view(), name='password_change'),
  path('password/change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
