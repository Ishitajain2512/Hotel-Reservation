from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_room, name='book_room'),
    path('success/', views.booking_success, name='success'),
    path('', views.book_room, name='book_room'),
    path('randomize/', views.random_occupancy, name='randomize_rooms'),
    path('reset/', views.reset_bookings, name='reset_bookings'),
]
