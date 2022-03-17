from dataclasses import fields
from rest_framework import serializers
from django_pro1_iot.rooms.models import Room
from django_pro1_iot.iotdevices.models import Devices


class IotDevicesSerializer(serializers.ModelSerializer):
    room = serializers.CharField(source='room.room_name', required = False, read_only=True)
    user  = serializers.CharField(source='room.user', required = False, read_only=True)
    class Meta:
        model = Devices
        fields = [ "id", "user", "room", "device_name",  "slug", "topic", "serial_id", "ip_address", "is_active", "is_on", "device_type", "created_at", "updated_at", "area_button1", "area_button2", "area_button3", "area_button4", "area_button5", "area_button6", "area_button7", "area_button8", "area_button9", "area_button10", "area_button11", "area_button12", "area_button13", "area_button14",]

class ListRoomsSerializer(serializers.ModelSerializer):
    devices_in_room = IotDevicesSerializer(many=True, required = False)
    user = serializers.CharField(source="user.username", required = False)

    class Meta:
        model = Room
        fields = [ "user", "room_name", "id",  "devices_in_room",  "slug", "description", "room_image",]