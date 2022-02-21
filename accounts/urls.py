from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "accounts"
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('create/', SignUpView.as_view(), name='create'),
    path('home/', UserHome.as_view(), name='user_home'),
    ]