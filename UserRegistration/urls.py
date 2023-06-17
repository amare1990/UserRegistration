from django.contrib import admin
from django.urls import path, include
from Users import views as user_view
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	path('admin/', admin.site.urls),
	path('', include('Users.urls')),
	path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='user/templates/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
