from django.shortcuts import render, redirect
from .models import Room, Booking
from .forms import BookingForm
from itertools import combinations

def calculate_travel_time(rooms):
    floors = set(room.floor for room in rooms)
    vertical_time = (max(floors) - min(floors)) * 2 if len(floors) > 1 else 0
    horizontal_time = 0
    if len(floors) == 1:
        numbers = sorted(int(room.number) % 100 for room in rooms)
        horizontal_time = numbers[-1] - numbers[0]
    else:
        horizontal_time = len(rooms) - 1
    return vertical_time + horizontal_time

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room_count = form.cleaned_data['room_count']
            available_rooms = Room.objects.filter(is_available=True)

            best_combo = None
            best_time = float('inf')
            for combo in combinations(available_rooms, room_count):
                travel_time = calculate_travel_time(combo)
                if travel_time < best_time:
                    best_time = travel_time
                    best_combo = combo

            if best_combo:
                booking = form.save(commit=False)
                booking.total_travel_time = best_time
                booking.save()
                for room in best_combo:
                    room.is_available = False
                    room.save()
                    booking.rooms.add(room)
                return redirect('success')
            else:
                form.add_error(None, "Not enough rooms available.")
    else:
        form = BookingForm()
    return render(request, 'booking/book_room.html', {'form': form})

def booking_success(request):
    return render(request, 'booking/success.html')
