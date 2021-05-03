from django.urls import path
from difference_detector import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.difference_detector, name='difference_detector'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
