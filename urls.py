from django.conf.urls import url
from .views import casita, formi, loggeate, logeado, loggout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^casi', casita),
    url(r'^formi', formi.as_view()),
    url(r'^loggin', loggeate.as_view()),
    url(r'^logeado',logeado),
    url(r'^loggout', loggout)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
