from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import links.views
import notes.views
import services.views


urlpatterns = [
    path('services/calculator_days', services.views.calculator),
    path('links/', links.views.index),
    path('notes/', notes.views.index),
    path('services/', services.views.index),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
]
