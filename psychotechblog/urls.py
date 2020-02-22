from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from wpisy import views as wpisy_widok


urlpatterns = [
    path('admin/', admin.site.urls),
    path('konta/', include('konta.urls')),
    path('wpisy/', include('wpisy.urls')),
    path('onas/', views.onas),
    path('',wpisy_widok.wpisy_list, name='Start'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)