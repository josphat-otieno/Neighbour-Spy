from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile_view, name='profile'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
