
from django.contrib import admin
from django.urls import path
from games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('browse',views.browse,name='browse'),
    path('details',views.details,name='details'),
    path('profile',views.profile,name='profile'),
    path('streams',views.streams,name='streams'),
]
