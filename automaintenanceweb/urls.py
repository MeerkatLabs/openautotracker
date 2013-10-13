from django.conf.urls import patterns, include, url
from automaintenanceweb.openautotracker.views import LandingPage, PrivacyPage
from automaintenanceweb.openautotracker.views import ChangeLogPage, TermsOfServicePage

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^user/login/', 'django.contrib.auth.views.login',
    #
    #     {'template_name': 'login.html'}, name="user_login"),
    #
    # url(r'^user/logout/', 'django.contrib.auth.views.logout',
    #     {'next_page': '/user/login/'}, name="user_logout"),

    url(r'^user/', include('automaintenance.urls')),
    url(r'^gplus/', include('django_auth_addon.urls')),
    url(r'^licenses/', include('licenses.urls')),
    url(r'^account/', include('account.urls')),

    url(r'^$', LandingPage.as_view(), name='landing'),
    url(r'^privacy/$', PrivacyPage.as_view(), name='privacy'),
    url(r'^changelog/$', ChangeLogPage.as_view(), name='changelog'),
    url(r'^terms/$', TermsOfServicePage.as_view(), name='termsofservice'),

)
