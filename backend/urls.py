from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'backend.views.index'),
    url(r'^add_user/', 'backend.views.add_user'),
    url(r'^login/', 'backend.views.login'),
    url(r'^add_handout/', 'backend.views.put_handout'),
    url(r'^get_handout/', 'backend.views.get_handouts'),
    url(r'^get_classmates/', 'backend.views.get_classmates'),
    url(r'^send_invites/', 'backend.views.send_invites'),
    url(r'^get_invites/', 'backend.views.get_invites'),
    url(r'^get_documents/', 'backend.views.get_documents'),
    url(r'^poops/', 'backend.views.add'),
    url(r'^portal/', 'backend.views.portal'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web_login/', 'backend.views.web_login'),
    url(r'^home/', 'backend.views.home'),
    url(r'^web_register/', 'backend.views.web_register'),
    url(r'^old_home/', 'backend.views.old_home'),
)
