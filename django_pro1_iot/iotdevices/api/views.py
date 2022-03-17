from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django_pro1_iot.iotdevices.models import Devices
from .serializers import ListRoomsSerializer, IotDevicesSerializer
from rest_framework.permissions import IsAuthenticated
from django_pro1_iot.rooms.models import Room
from rest_framework.response import Response
from rest_framework import status

class List_Rooms(APIView):
    permission_classes = [IsAuthenticated]

    def get (self, request):
        rooms = Room.objects.filter(user=request.user)
        serializer = ListRoomsSerializer(rooms, many=True, context= {'request': request})
        return Response(serializer.data)

    def post (self, request):
            serializer = ListRoomsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
        

class Detail_Room(APIView):
    permission_classes = [IsAuthenticated]

    def get (self, request, room_pk):
        try:
            user = request.user
            room = Room.objects.get(pk=room_pk, user=user)
        except Room.DoesNotExist:
            return Response({"error": "Room does not exist ya sa7by"} ,status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListRoomsSerializer(room, context={"request": request})

        return Response(serializer.data, status=status.HTTP_302_FOUND)

  

    def put (self, request, room_pk):
        try:
            room = Room.objects.get(pk=room_pk, user=request.user)

        except Room.DoesNotExist:
            return Response({"error": "Room does not exist ya 7oby"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListRoomsSerializer(room ,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
    def delete (self, request, room_pk):
        try:
            room = Room.objects.get(pk=room_pk, user=request.user)

        except Room.DoesNotExist:
            return Response({"error": "Room does not exist ya sa7by"}, status=status.HTTP_404_NOT_FOUND)

        room.delete()
        return Response({"deleted successfuly": "delleted yas sa7by"}, status=status.HTTP_204_NO_CONTENT)




class List_Devices(APIView):
    permission_classes = [IsAuthenticated]
    
    def get (self, request, room_pk):
        try:
            user = request.user
            room = Room.objects.get(pk=room_pk, user=user)
            devices = Devices.objects.filter(room=room)
        except (Room.DoesNotExist, Devices.DoesNotExist):
            return Response({"error": "Room does not exist ya sa7by"} ,status=status.HTTP_404_NOT_FOUND)
        
        serializer = IotDevicesSerializer(devices, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def post (self, request, room_pk):
        serializer = IotDevicesSerializer(data=request.data)
        try:
            room = Room.objects.get(pk=room_pk, user=request.user)
        except (Room.DoesNotExist, Devices.DoesNotExist):
            return Response({"error": "Room does not exist ya sa7by"} ,status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save(room=room)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Detail_Device(APIView):
    permission_classes = [IsAuthenticated]
    
    def get (self, request, room_pk, device_pk):
        try:
            user = request.user
            room = Room.objects.get(pk=room_pk, user=user)
            device = Devices.objects.get(room=room, pk=device_pk)
        except (Room.DoesNotExist, Devices.DoesNotExist):
            return Response({"error": "Room does not exist ya sa7by"} ,status=status.HTTP_404_NOT_FOUND)
        
        serializer = IotDevicesSerializer(device, context={"request": request})

        return Response(serializer.data, status=status.HTTP_302_FOUND)



    def put (self, request, room_pk, device_pk):
        try:
            room = Room.objects.get(pk=room_pk, user=request.user)
            device = Devices.objects.get(pk=device_pk, room=room)
        except (Room.DoesNotExist, Devices.DoesNotExist):
            return Response({"error": "Room does not exist ya 7oby"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IotDevicesSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
    def delete (self, request, room_pk, device_pk):
        try:
            room = Room.objects.get(pk=room_pk, user=request.user)
            device = Devices.objects.get(pk=device_pk, room=room)
        except (Room.DoesNotExist, Devices.DoesNotExist):
            return Response({"error": "Room does not exist ya sa7by"}, status=status.HTTP_404_NOT_FOUND)

        device.delete()
        return Response({"deleted successfuly": "deleted yas sa7by"}, status=status.HTTP_204_NO_CONTENT)
