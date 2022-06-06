from django.urls import path 
from . import views 
from main_app.views import front


urlpatterns = [ 
    path('', front, name='front'),
    path('home/', views.Home.as_view(), name='home'),
    # path('landingpage/', views.Landing.as_view(), name='landing'),
    # path('accounts/signup/', views.Signup.as_view(), name='signup')
]