from django.urls import path
from .views import user_registration_view, logut_view
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('logout/', logut_view, name='logout'),
    path('register/', user_registration_view, name='register'),

]