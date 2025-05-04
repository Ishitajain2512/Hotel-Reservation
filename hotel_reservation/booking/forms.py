from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    room_count = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Number of Rooms",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of Rooms'
        })
    )

    class Meta:
        model = Booking
        fields = ['guest_name', 'check_in', 'check_out']

        widgets = {
            'guest_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Guest name'
            }),
            'check_in': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Check-in date',
                'id': 'id_check_in'
            }),
            'check_out': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Check-out date',
                'id': 'id_check_out'
            }),
        }
