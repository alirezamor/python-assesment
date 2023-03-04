from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Listing, Room, Reservation

from django.shortcuts import render
from .models import Listing, Room, Reservation
from .serializers import *


class ReservationView(APIView):
    
    def post(self, request):
        serializer = ReservationSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        res = serializer.create(serializer.validated_data)
        return res


@api_view(['GET'])
def check_availability(request):
    room_id = request.query_params['room_id']
    start_time = request.query_params['start_time']
    end_time = request.query_params['end_time']

    room = get_object_or_404(Room, id=room_id)

    if room.reservations.filter(start_time__lte=end_time, end_time__gte=start_time).exists():
        return Response({'available': False})
    else:
        return Response({'available': True})
            
        
def overview(request):
    listings = Listing.objects.all()
    reservations = Reservation.objects.all()
    context = {'listings': listings, 'reservations': reservations}
    return render(request, 'overview.html', context)

def overview_text(request):
    listings = Listing.objects.all()
    reservations = Reservation.objects.all()
    context = {'listings': listings, 'reservations': reservations}
    return render(request, 'overview.txt', context, content_type='text/plain')
