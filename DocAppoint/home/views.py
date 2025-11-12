from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Departments, Doctors
from .forms import BookingForm
# from .models import Booking



def home_views(request):
    return render(request, 'home.html')


def about_views(request):
    return render(request, 'about.html')


def contact_views(request):
    return render(request, 'contact.html')

 
def booking_views(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Admin Email Content
            subject = f'New Appointment Booking for {booking.doctor}'
            message = f'''
            A new booking has been made.

            Patient Name: {booking.patient_name}
            Patient Phone: {booking.patient_phone}
            Patient Email: {booking.patient_email}
            Doctor: {booking.doctor}
            Department: {booking.doctor.dep_name}
            Booking Date: {booking.booking_date}
            '''
            from_email = 'irashimuhammed@gmil.com'
            recipient_list = ['mi6909741@gmail.com']

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # --- Optional: Confirmation Email to User ---
            user_subject = 'Your Appointment is Confirmed!'
            user_message = f'''
            Dear {booking.patient_name},

            Thank you for booking an appointment with us.
            Your appointment with {booking.doctor} on {booking.booking_date} is confirmed.

            We look forward to seeing you.
            '''
            user_recipient_list = [booking.patient_email]

            send_mail(user_subject, user_message, from_email, user_recipient_list, fail_silently=False)
            # --- End of Optional Part ---

            return redirect('confirmation')
    else:
        form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


def doctors_views(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)


def department_views(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)

def confirmation_views(request):
    return render(request, 'confirmation.html')