from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'muni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.lista_publicaciones),
	
]
