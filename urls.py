from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^guest$', 'guestbook.views.guestbook'),                        
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
                       
)
