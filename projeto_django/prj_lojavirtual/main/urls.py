from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)