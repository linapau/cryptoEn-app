"""
URL configuration for ssd_encryption project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from data.urls.urls import router
from data.views import views_user, views_file


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data.urls.urls')),
    path('register/', views_user.register_user, name='register'),
    path('login/', views_user.login_user, name='login'),
    path('logout/', views_user.logout_user, name='logout'),
    path('update-profile/', views_user.update_profile, name='update_profile'),
    path('upload_file/', views_file.upload_file, name='upload_file'),
    path('browse_files/', views_file.browse_files, name='browse_files'),
    path('', views_file.upload_file, name='upload_file'),
]