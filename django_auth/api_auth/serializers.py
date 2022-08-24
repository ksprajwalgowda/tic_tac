from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import UserDetails

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserDetailsSerializer(serializers.ModelSerializer):
  uploaded_image = serializers.FileField(
        max_length = 1000000,
        allow_empty_file = False,
        write_only = True
    )
  profile_image = UserSerializer(read_only = True)
  class Meta:
    model = UserDetails
    fields = ('email', 'username','first_name','last_name', 'dob','gender', 'bio', 'phone_no','profile_image','uploaded_image')
    extra_kwargs = {
            'image': { 'read_only': True }
        }

  def create(self, validated_data):
    image_data = validated_data.pop('uploaded_image')
    thread_obj = UserDetails(**validated_data)
    thread_obj.image = image_data
    thread_obj.save()
    return thread_obj