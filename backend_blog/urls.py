from django.contrib import admin
from django.urls import path, include  # ← Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_blog.urls')),  # ← Incluye las rutas de app_blog
]