"""
    proyecto/urls.py: 
                    Las declaraciones URL para este proyecto Django; 
                    una «tabla de contenidos» de su sitio basado en Django
"""

"""
    Señalización de las URLconf del modulo app/urls
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
]