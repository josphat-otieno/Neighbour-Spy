from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_vies
urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_vies.LogoutView.as_view(), {'next_page':'/accounts/register/'}),
    url(r'^profile/$', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('search/', views.search_business, name='search'),
    url(r'^new/neighbor', views.new_neighbor, name='neighbor'),
    url(r'^neighbor/(\d+)/$',views.neighborhood_view,name ='neighbor-detail'),
    path('delete/<int:neighborhood_id>/', views.delete_neighborhood, name='delete_neighborhood'),
    url(r'^(?P<neighborhood_id>[0-9]+)/count$', views.update_count, name="update_count"),
    url(r'^(?P<neighborhood_id>[0-9]+)/business$', views.create_business, name="create_business"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
