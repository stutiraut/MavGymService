from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


time = (
    ('7:00 am - 8:00 am', '7:00 am - 8:00 am'),
    ('8:00 am - 9:00 am', '8:00 am - 9:00 am'),
    ('9:00 am - 10:00 am', '9:00 am - 10:00 am'),
    ('10:00 am - 11:00 am', '10:00 am - 11:00 am'),
    ('11:00 am - 12:00 pm', '11:00 am - 12:00 pm'),
    ('12:00 pm - 1:00 pm', '12:00 pm - 1:00 pm'),
    ('1:00 pm - 2:00 pm', '1:00 pm - 2:00 pm'),
    ('2:00 pm - 3:00 pm', '2:00 pm - 3:00 pm'),
    ('3:00 pm - 4:00 pm', '3:00 pm - 4:00 pm'),
    ('4:00 pm - 5:00 pm', '4:00 pm - 5:00 pm'),

)

activity = (
    ('zumba class', 'ZUMBA CLASS'),
    ('swimming class', 'SWIMMING CLASS'),
    ('basketball match', 'BASKETBALL MATCH'),
    ('yoga class', 'YOGA CLASS'),
    ('dancing class', 'DANCING CLASS'),

)

location = (
    ('MGS Room 101', 'MGS Room 101'),
    ('MGS Room 102', 'MGS Room 102'),
    ('MGS Room 103', 'MGS Room 103'),
    ('MGS Room 104', 'MGS Room 104'),
    ('MGS Room 105', 'MGS Room 105'),

)

weights =(

    ('5 pound', '5 pound'),
    ('10 pound', '10 pound'),
    ('50 pound', '50 pound'),
    ('100 pound', '100 pound'),
    )




# Create your models here.
# Staff module
class Staff(models.Model):
    staff_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff')
    staff_street = models.CharField(max_length=50)
    staff_city = models.CharField(max_length=50)
    staff_state = models.CharField(max_length=50)
    staff_zip = models.CharField(max_length=10)
    staff_email = models.CharField(max_length=50)
    staff_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.staff_name)


# Customer module
class Customer(models.Model):
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    customer_street = models.CharField(max_length=50)
    customer_city = models.CharField(max_length=50)
    customer_state = models.CharField(max_length=50)
    customer_zip = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_name)



# Availability module
class Availability(models.Model):
    availability_staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='availabilities')
    activity = models.CharField(max_length=100, choices=activity, default='zumba class')
    time = models.CharField (max_length=100,choices=time,default='7:00 am - 8:00 am' )
    location = models.CharField(max_length=100, choices=location, default='MGS Room 101')
    start_date = models.DateField(blank=True, default=timezone.now)
    created_date = models.DateField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()
    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    @property
    def get_html_url(self):
        url = reverse('gym:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.activity}-{self.time}-{self.location} </a>'


class GymEquipment(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='equipments', null=True, blank=True,default=None)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    weight = models.CharField(max_length=100, choices=weights, default='5 pound')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.weight)
