from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
import services.views
import contact.views
import gallery.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', services.views.home, name='home'),
    url(r'^services/', services.views.services, name='services'),
    url(r'^about/', services.views.about, name='about'),
    url(r'^contact/', contact.views.contact, name='contact'),
    url(r'^gallery/', gallery.views.gallery, name='gallery'),
    url(r'^service_detail/(?P<slug>[\w-]+)/$', services.views.service_detail, name='service_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
