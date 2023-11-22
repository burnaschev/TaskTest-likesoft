from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializers
from users.tasks import send_welcome_email


class UserCreateAPIViewSet(generics.CreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Отправка сообщения регистраций на веб сервисе"""
        user = serializer.save()
        send_welcome_email.delay(user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
