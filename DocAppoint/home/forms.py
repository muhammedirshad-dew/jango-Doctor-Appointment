from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['patient_name', 'patient_phone', 'patient_email', 'doctor', 'booking_date']
        widgets = {
            'booking_date': DateInput(),
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
        }

        labels ={
            'patient_name': 'Full Name',
            'patient_phone': 'Phone Number',
            'patient_email': 'Email Address',
            'doctor': 'Select Doctor',
            'booking_date': 'Preferred Date',   
        }