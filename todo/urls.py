from django.contrib import admin
from django.urls import path,include
from todo import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path("agregar/",views.agregar,name="agregar"),
    
]
