from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'Main.views.main_page'),

                       # Login / logout.
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^register/$', 'Main.views.register'),
    (r'^register_success/$', 'Main.views.register_success'),

    # Examples:
     url(r'^writigain/$', 'Writigain.views.index', name='writigain'),
     url(r'^listigain/$', 'Listigain.views.index', name='listigain'),
    url(r'^listigain/add$', 'Listigain.views.add', name='add'),
    url(r'^listigain/(?P<task_id>\d+)/delete$', 'Listigain.views.delete', name='delete'),
    url(r'^listigain/(?P<task_id>\d+)/edit$', 'Listigain.views.edit', name='edit'),
     url(r'^main/$', 'Main.views.index', name='main'),
    url(r'^listigain/initialize_quad$', 'Listigain.views.initialize_quad', name='initialize_quad'),
    url(r'^listigain/(?P<task_id>\d+)/return_quad$', 'Listigain.views.return_quad', name='return_quad'),
    url(r'^listigain/quad$', TemplateView.as_view(template_name="quad.html")),


    # url(r'^Procrastigain/', include('Procrastigain.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   # url(r'^admin/', include(admin.site.urls)),
)
