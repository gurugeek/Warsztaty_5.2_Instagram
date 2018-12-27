from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('user_insta/', UserInstaView.as_view(), name='user-insta'),
]
