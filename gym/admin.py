from django.contrib import admin

from .models import Staff, Customer, Availability, GymEquipment
# Register your models here.
# Staff model
@admin.register(Staff)
class StaffList(admin.ModelAdmin):
    list_display = ('staff_name', 'staff_email', 'staff_phone')
    list_filter = ('staff_name',)
    search_fields = ('staff_name',)
    ordering = ['staff_name']

# customer model
@admin.register(Customer)
class CustomerList(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_phone')
    list_filter = ('customer_name',)
    search_fields = ('customer_name',)
    ordering = ['customer_name']


# Availability model
@admin.register(Availability)
class AvailabilityList(admin.ModelAdmin):
    list_display = ('availability_staff_name', 'activity', 'time','start_date')
    list_filter = ('availability_staff_name','time',)
    search_fields = ('availability_staff_name','time')
    ordering = ['availability_staff_name','time']


# Appointment model
@admin.register(GymEquipment)
class GymEquipmentList(admin.ModelAdmin):
    list_display = ('name', 'description', 'weight')
    list_filter = ('weight',)
    search_fields = ('weight',)
    ordering = ['weight']
