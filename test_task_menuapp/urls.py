from django.contrib import admin
from django.urls import path
from menu_app.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu_app/', menu),
]
