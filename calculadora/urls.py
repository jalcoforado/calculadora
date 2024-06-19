from django.contrib import admin
from django.urls import include, path
from AppCalculadora import views
urlpatterns = [
    path('', include('AppCalculadora.urls')),  # Aqui estamos incluindo novamente para a rota raiz    
    path('AppCalculadora/', include('AppCalculadora.urls')),  
    path('admin/', admin.site.urls),
    
]
