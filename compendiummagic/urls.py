from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'compendiummagic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^compendiummagic/', include('compendium.urls'), name='compendium'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]
