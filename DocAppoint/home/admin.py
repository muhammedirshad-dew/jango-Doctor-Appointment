from django.contrib import admin
from . models import Departments, Doctors, Booking

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'patient_phone', 'patient_email', 'doctor__doc_name', 'booking_date', 'booked_on')
admin.site.register(Booking, BookingAdmin)
