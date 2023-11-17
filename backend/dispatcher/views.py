from django.shortcuts import render, get_object_or_404
from django_chat.views import room
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .models import Dispatcher
from drivers.models import Driver
from rest_framework import generics, permissions
from django.db import IntegrityError
from rest_framework import serializers
from .models import Dispatcher


class DispathcerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatcher
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
            "user_type",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "user_type": {"read_only": True},
        }

    def create(self, validated_data):
        try:
            password = validated_data.pop("password")
            instance = Dispatcher.objects.create(**validated_data)
            instance.user_type = "dispathcer"
            instance.set_password(password)
            instance.save()

        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            raise serializers.ValidationError({"email": ["exists"]})
        return instance


class DispatcherRegistrationView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DispathcerSerializer
    permission_classes = [permissions.IsAdminUser]


@login_required
def driver_dispatcher_room(request, user_id):
    if request.user.user_type == "driver":
        driver = request.user
        dispatcher = get_object_or_404(Dispatcher, id=user_id)

    elif request.user.user_type == "dispatcher":
        dispatcher = request.user
        driver = get_object_or_404(Driver, id=user_id)

    else:
        return Response({"message": "You are not allowed to chat with others"})

    room_name = f"{driver.email}_{dispatcher.email}"
    return room(request, room_name)
