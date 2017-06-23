"""kma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from kma import settings

urlpatterns = [
    # url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index'),
    url(r'^news/$', 'main.views.news'),
    url(r'^about/$', 'main.views.about'),
    url(r'^acts/$', 'main.views.acts'),
    url(r'^nmo/$', 'main.views.nmo'),
    url(r'^pdmo/$', 'main.views.pdmo'),
    url(r'^attestation/$', 'main.views.attestation'),
    url(r'^article/(\d+)/$', 'main.views.article'),
    url(r'^act/(\d+)/$', 'main.views.act'),
    url(r'^protocol/(\d+)/$', 'main.views.protocol'),
    url(r'^nmo/(\d+)/$', 'main.views.nmo1'),
    url(r'^pdmo/(\d+)/$', 'main.views.pdmo1'),
    url(r'^attestation/(\d+)/$', 'main.views.attestation1'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
