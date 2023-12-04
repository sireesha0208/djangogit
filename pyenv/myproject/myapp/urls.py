from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('section1/', views.section1,name = 'section 1')
]