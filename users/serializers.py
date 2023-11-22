from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'registration_date']
        extra_kwargs = {
            'username': {'required': True}
        }

