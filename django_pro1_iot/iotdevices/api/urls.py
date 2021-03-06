from django.urls import path
from .views import List_Rooms, Detail_Room, List_Devices, Detail_Device, Alexa_Esp_Model

urlpatterns = [
    path("rooms/", List_Rooms.as_view(), name="list_rooms"),
    path("rooms/<int:room_pk>/", Detail_Room.as_view(), name="detail_rooms"),
    path("rooms/<int:room_pk>/devices/", List_Devices.as_view(), name="list_devices"),
    path(
        "rooms/<int:room_pk>/devices/<int:device_pk>/",
        Detail_Device.as_view(),
        name="detail_devices",
    ),
    path(
        "call_esp_model/",
        Alexa_Esp_Model.as_view({"get": "list"}),
        name="call_esp_model",
    ),
]
