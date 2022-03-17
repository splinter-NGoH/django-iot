from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }
    



class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            "password": {"write_only": True}
        }


    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error": "password didn't match idiot"})
        
        if User.objects.filter(email=self.validated_data['email']):
            raise serializers.ValidationError({"error": "idiot email already exist"})

        if User.objects.filter(username=self.validated_data['username']):
            raise serializers.ValidationError({"error": "idiot username already exist"})

        user_create = User(email=self.validated_data['email'], username=self.validated_data['username'])
        user_create.set_password(password)
        user_create.save()

        return user_create