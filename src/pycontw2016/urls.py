from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import set_language

from core.views import flat_page, index, staff
from users.views import user_dashboard


urlpatterns = i18n_patterns(

    # Add top-level URL patterns here.
    url(r'^$', index, name='index'),
    url(r'^dashboard/$', user_dashboard, name='user_dashboard'),
    url(r'^accounts/', include('users.urls')),
    url(r'^proposals/', include('proposals.urls')),

    url(r'^about/staff/$', staff),

    # Match everything except admin, media, and static things.
    url(r'^(?!admin|{media}|{static}/)(?P<path>.*)/$'.format(
        media=settings.MEDIA_URL.strip('/'),
        static=settings.STATIC_URL.strip('/')),
        flat_page, name='page'),
)

# set-langauge and admin should not be prefixed with language.
urlpatterns += [
    url(r'^set-language/$', set_language, name='set_language'),
    url(r'^admin/', include(admin.site.urls)),
]

# User-uploaded files like profile pics need to be served in development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
