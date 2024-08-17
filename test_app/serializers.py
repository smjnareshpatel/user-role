from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('username','email','role')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'username',
            'role'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            role=validated_data['role'],
            is_active=True,
        )
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email = data['email'])
            if not user.is_active:
                raise serializers.ValidationError("User is not active.")
        except User.DoesNotExist as ex:
            raise serializers.ValidationError("User not registered.")

        # user = authenticate(username=data['username'],password=data['password'])
        check_user = user.check_password(data['password'])
        print(data,'================',check_user)
        if check_user is None:
            raise serializers.ValidationError("Invalid Credentials.")

        elif check_user and user.is_active:
            
            return user