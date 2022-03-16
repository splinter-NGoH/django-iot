from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, UserRegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)



@api_view(['POST',])
def user_registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user_create = serializer.save()
            data['response'] = "Registration successful ya sa7by <3"
            data['username'] = user_create.username
            data['email'] = user_create.email
            token = Token.objects.get(user=user_create).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data, status= status.HTTP_201_CREATED)


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def logut_view (request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {"Token Deleted": "kda anta logedout, a7b afakrk al b3na 5esr dl3na"}
        return Response(data,status=status.HTTP_200_OK)
