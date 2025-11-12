from django.db import models

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors/')
    
    def __str__(self):
        return f'Dr. {self.doc_name}'

class Booking(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=10)
    patient_email = models.EmailField()
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.patient_name} - {self.doctor} on {self.booking_date}'

   