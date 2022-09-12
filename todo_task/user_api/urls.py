from django.urls import path
from .views import *

urlpatterns = [
    path('add_user/', UserAPI.as_view()), # New user registration - POST request
    path('login_user/', UserLogin.as_view()),   # Login with email_id and password - POST request
]