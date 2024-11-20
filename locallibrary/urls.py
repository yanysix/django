from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Включает URL для входа, выхода и т.д.
    path('accounts/logout/',
         LogoutView.as_view(template_name='registration/logged_out.html'),
         name='logout'),  # Настройка URL для выхода
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
