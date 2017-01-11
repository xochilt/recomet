from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf.urls.static import static
import settings
from settings import STATIC_URL, STATIC_ROOT
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^recomet/$', 'restaurant.views.index', name='index'),
    url(r'^accounts/login/$',  'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',  {'next_page': '/accounts/login/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^recomet/rating/$', 'restaurant.views.addRatingIndex'),
    url(r'^recomet/helpful/$', 'restaurant.views.isHelpful'),   
    
    url(r'^recomet/user/profile/(?P<iduser>\d+)/$', 'restaurant.views.temp_user'),
    #Ver el perfil del restaurante.
    url(r'^recomet/view_profile/(?P<id>\d+)/$', 'restaurant.views.view_profile'),
    #Formulario modal para insercion de reviews.
    url(r'^recomet/addreviewmodal/(?P<id>\d+)/$', 'restaurant.views.addreviewmodal'),

    #URLs del perfil dl usuario.
    #menu: Reviews/Ratings/Wishlist/
    url(r'^recomet/wishlist/(?P<iduser>\d+)/$', 'restaurant.views.wishlist'),#Reviews
    url(r'^recomet/addwish/$','restaurant.views.addwish'), 
    url(r'^recomet/addwish3/$','restaurant.views.addwish3'),
    url(r'^recomet/deletewishlist/$','restaurant.views.delete_wishlist'),
    url(r'^recomet/deleteall/$','restaurant.views.delete_all'),
    
    #Recomendaciones de los invitados
    url(r'^recomet/guest/$', 'restaurant.views.recomguest'),
    url(r'^recomet/topten/$', 'restaurant.views.topten'),
    
    #registration module
    url(r'^accounts/', include('registration.backends.default.urls')),
    #Verificar si no afecta al registro del usuario cuando usa  el modulo de registro.
    #url(r'^accounts/profile/(?P<iduser>\d+)/$', 'restaurant.views.userprofile'),
    url(r'^recomet/usercontext/(?P<iduser>\d+)/$', 'restaurant.views.userprofile'),
    url(r'^recomet/recomtest/$', 'restaurant.views.recomtest'),
    url(r'^recomet/location/$', 'restaurant.views.currentlocation'),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


