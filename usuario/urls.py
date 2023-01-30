from django.urls import path
from usuario.views import Login, Logout
# from django.contrib.auth import views as auth_views


urlpatterns = [

    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name='logout'),
    
   
]