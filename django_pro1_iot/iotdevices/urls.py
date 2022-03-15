from django.urls import path

from django_pro1_iot.users.views import (
    iotdevices,
)

app_name = "users"
urlpatterns = [
    path("iotdevices/", view=iotdevices, name="iotdevices"),

]
