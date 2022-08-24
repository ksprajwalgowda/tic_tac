from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.helloView, name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), #login
    path('create_auth/', views.create_auth, name='create_auth' ), #signup
    path('set_password/', views.set_password, name='set_password'), #change password
    path('logout/',views.logout, name='logout'), #logout
    path('userdetails/',views.create_userDetails, name='create_userDetails'), #create_userDetails
]