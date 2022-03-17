from django.db import models
from django_pro1_iot.users.models import User
from django_pro1_iot.rooms.models import Room


class Devices(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='devices_in_room')
    device_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    serial_id = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_on = models.BooleanField(default=False)
    device_type = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    area_button1 = models.CharField(max_length=255, null=True, blank=True)
    area_button2 = models.CharField(max_length=255, null=True, blank=True)
    area_button3 = models.CharField(max_length=255, null=True, blank=True)
    area_button4 = models.CharField(max_length=255, null=True, blank=True)
    area_button5 = models.CharField(max_length=255, null=True, blank=True)
    area_button6 = models.CharField(max_length=255, null=True, blank=True)
    area_button7 = models.CharField(max_length=255, null=True, blank=True)
    area_button8 = models.CharField(max_length=255, null=True, blank=True)
    area_button9 = models.CharField(max_length=255, null=True, blank=True)
    area_button10 = models.CharField(max_length=255, null=True, blank=True)
    area_button11 = models.CharField(max_length=255, null=True, blank=True)
    area_button12 = models.CharField(max_length=255, null=True, blank=True)
    area_button13 = models.CharField(max_length=255, null=True, blank=True)
    area_button14 = models.CharField(max_length=255, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.device_name

    
