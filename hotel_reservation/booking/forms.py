from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    room_count = forms.IntegerField(min_value=1, max_value=5, label="Number of Rooms")

    class Meta:
        model = Booking
        fields = ['guest_name', 'check_in', 'check_out']
