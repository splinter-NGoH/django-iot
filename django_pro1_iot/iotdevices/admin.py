from django.contrib import admin
from .models import Devices


class DeviceAdmin(admin.ModelAdmin):
    list_display = [ "room", "device_name", "serial_id", "is_active", "is_on", "device_type", "created_at"]
    search_fields = ["device_name", "serial_id", "is_active", "is_on"]
    filter_fields = ["is_active", "is_on", "device_type", "created_at", "updated_at",]
    prepopulated_fields = {"slug": ("device_name",)}




admin.site.register(Devices, DeviceAdmin)