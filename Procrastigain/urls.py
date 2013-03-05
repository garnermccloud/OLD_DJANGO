from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'Main.views.main_page'),

                       # Login / logout.
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^register/$', 'Main.views.register'),
    (r'^register_success/$', 'Main.views.register_success'),

    # Examples:
     url(r'^writigain/$', 'Writigain.views.index', name='home'),
     url(r'^listigain/$', 'Listigain.views.index', name='home'),
    url(r'^listigain/add$', 'Listigain.views.add', name='home'),
    url(r'^listigain/(?P<task_id>\d+)/delete$', 'Listigain.views.delete', name='home'),
     url(r'^main/$', 'Main.views.index', name='home'),

    # url(r'^Procrastigain/', include('Procrastigain.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   # url(r'^admin/', include(admin.site.urls)),
)
