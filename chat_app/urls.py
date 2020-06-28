from django.urls import path
from . import views


urlpatterns = [
    path('', views.MessagesListView.as_view(), name='index')
]