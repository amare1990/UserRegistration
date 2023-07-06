from django.contrib import admin
from django.urls import path, include
from Users import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from Users.views import MyPasswordChangeView, custom_password_change_done
from django.contrib.auth.views import PasswordChangeDoneView

# from .views import custom_password_change_done

urlpatterns = [

	path('admin/', admin.site.urls),
	path('', include('Users.urls')),
	path('login/', user_view.Login, name ='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name ='user/templates/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),
  path('accounts/', include('allauth.urls')),

	# Password reset URLs
	path('password_reset/', user_view.CustomPasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	path('password/change/', MyPasswordChangeView.as_view(), name='password_change'),
  path('password/change/done/', user_view.custom_password_change_done, name='password_change_done'),

	path('upload/',user_view.upload_photo, name='upload_photo'),
  path('photo_list/', user_view.photo_list_view, name='photo_list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
