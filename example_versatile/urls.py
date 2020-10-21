from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from example_versatile.images.views import index_view, form_view

urlpatterns = [
    url('^$', index_view),
    url('^add$', form_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
