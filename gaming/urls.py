
from django.contrib import admin
from django.urls import path , include
from games import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('browse',views.browse,name='browse'),
    path('games',views.games,name='games'),
    path('details/<int:id>/',views.details,name='game_detail'),
    path('details',views.details,name='details'),
    path('profile',views.profile,name='profile'),
    path('streams',views.streams,name='streams'),
    path('categories',views.categories,name='categories'),
    path('login',views.login,name='login'),
    path('accounts/',include('accounts.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
