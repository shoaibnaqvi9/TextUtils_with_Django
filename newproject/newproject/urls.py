from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   path('contact/', views.contact, name='contact'),
   path('about/', views.about, name='about'),
   path("analyze" , views.analyze , name = "analyze")
]

