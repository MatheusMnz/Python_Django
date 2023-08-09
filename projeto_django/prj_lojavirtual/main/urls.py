from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]