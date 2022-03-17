from django.contrib import admin
from .models import Room
class RoomAdmin(admin.ModelAdmin):
    list_display = ["user", "room_name", "description", "slug"]
    search_fields = ["room_name",]
    prepopulated_fields = {"slug": ("room_name",)}



admin.site.register(Room, RoomAdmin)
