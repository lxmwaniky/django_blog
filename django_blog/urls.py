from django.contrib import admin
from django.urls import path, include
from users.views import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', include('blog.urls')),
]
