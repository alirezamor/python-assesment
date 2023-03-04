from django.urls import path
from . import views

urlpatterns = [
    path('make_reservation/', views.ReservationView.as_view(), name='make_reservation'),
    path('check_availability/', views.check_availability, name='check_availability'),
    path('overview/', views.overview, name='overview'),
    path('overview_text/', views.overview_text, name='overview_text'),
]
