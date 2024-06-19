from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from data.views import views_user, views_file


router = DefaultRouter()
router.register(r'users', views_user.UserViewSet, basename='user')


urlpatterns = [
    #path('', include(router.urls)),
    path('', views_file.upload_file, name='upload_file'),
    path('upload_file/', views_file.upload_file, name='upload_file'),
    path('download_file/<str:file_name>/', views_file.download_file, name='download_file'),
    path('browse_files/', views_file.browse_files, name='browse_files'),
    path('list_files/', views_file.list_files, name='list_files'),  # New endpoint
]