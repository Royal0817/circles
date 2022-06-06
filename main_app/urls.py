from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.Home.as_view(), name='home'),
    path('landingpage/', views.Landing.as_view(), name='landing'),
]