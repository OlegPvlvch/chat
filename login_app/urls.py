from django.urls import path
from django.contrib.auth import views as v
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.MyLoginView.as_view(), name='signin'),
    path('logout/', v.LogoutView.as_view(), name='logout')
]