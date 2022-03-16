from django.urls import path
from .views import user_registration_view
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),

    path('register/', user_registration_view, name='register'),

]