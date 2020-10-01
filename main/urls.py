from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # path('home/', include('home.urls')),
    path('', views.homepage),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]