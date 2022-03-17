from django.db import models
from django_pro1_iot.users.models import User

class Room(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rooms')
    room_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    room_image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.room_name
        


