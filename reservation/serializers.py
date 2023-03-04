from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, APIException

from .models import Reservation, Room


class ReservationSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    start_time = serializers.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
    end_time = serializers.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    def create(self, validated_data):
        room_id = validated_data.get('room_id')
        name = validated_data.get('name')
        start_time = validated_data.get('start_time')
        end_time = validated_data.get('end_time')

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise NotFound(detail= "Room with this id does not exist")

        if room.reservations.filter(start_time__lte=end_time, end_time__gte=start_time).exists():   
            raise APIException(detail= 'Room is already booked for this time period')

        reservation = Reservation.objects.create(room=room, name=name, start_time=start_time, end_time=end_time)
        return Response(data={'reservation_id': reservation.id}, status=status.HTTP_201_CREATED)
