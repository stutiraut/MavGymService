from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.views import generic
from .forms import RegisterForm , EventForm , EventEditForm
from .models import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
import calendar
from .forms import User
from .forms import Availability
from .utils import Calendar,CustomerCalendar
from datetime import datetime, timedelta, date
from django.urls import reverse
from .forms import UserEditForm
from django.template.loader import get_template
from .utils import render_to_pdf
from .forms import *
from django.db.models import Q



now = timezone.now()
def home(request):
   return render(request, 'gym/home.html',
                 {'gym': home})

def register(request):
    print("entered into register view method")
    if request.method == 'POST':
        print("entered into register view method entered if method")
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,
                          'registration/registerdone.html',
                          {'form': form})
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


class CalendarView(generic.ListView):
    model = Availability
    template_name = 'gym/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        staff = Staff.objects.get(staff_name_id=self.request.user.id)
        cal = Calendar(d.year, d.month, staff.id)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


class CalendarCustomerView(generic.ListView):
    model = Availability
    template_name = 'gym/viewCalendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = CustomerCalendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['customercalendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event_new(request, event_id=None):
    instance = Availability()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        availform = form.save ( commit=False )
        staff=Staff.objects.get ( staff_name_id=request.user.id )
        availform.availability_staff_name_id = staff.id
        today = date.today()
        first_day = today.replace(day=1)
        thisMonthDate = first_day
        #alreadyDataCount = Availability.objects.filter ( availability_staff_name_id = staff.id,start_date= availform.start_date).count ( )
        #if(alreadyDataCount==0):
        if (availform.start_date >= thisMonthDate):
            availform.save ( )
            return HttpResponseRedirect ( reverse ( 'gym:calendar' ) )
        else:
            messages.error ( request , 'Cannot add availability for previous month..' )
            return render(request, 'gym/event.html', {'form': form})

    return render(request, 'gym/event.html', {'form': form})

def event_edit(request, event_id):

    instance = get_object_or_404(Availability, pk=event_id)
    form = EventEditForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        availform = form.save ( commit=False )
        staff=Staff.objects.get ( staff_name_id=request.user.id )
        availform.availability_staff_name_id = staff.id
        availform.save ( )
        return HttpResponseRedirect ( reverse ( 'gym:calendar' ) )
    return render(request, 'gym/event.html', {'form': form})

def event_delete(request,pk):
    instance = Availability ( )
    event = get_object_or_404 ( Availability , pk=pk )
    event.delete ( )
    return HttpResponseRedirect(reverse('gym:calendar'))

@login_required
def CustomerViewActivities(request):
    availabilities = Availability.objects.filter(created_date__lte=timezone.now())
    return render(request, 'gym/CustomerViewActivities.html',
                 {'availabilities': availabilities})

@login_required
def users_list(request):
    users = User.objects.all()
    #print(users)
    return render(request, 'gym/users_list.html', {'users': users})

@login_required
def user_edit(request, pk):
   user = get_object_or_404(User, pk=pk)
   if request.method == "POST":
       # update
       form = UserEditForm(request.POST, instance=user)
       if form.is_valid():
           user = form.save(commit=False)
           user.updated_date = timezone.now()
           user.save()
           users = User.objects.filter()
           print(users)
           return render(request, 'gym/users_list.html',
                         {'users': users})
   else:
        # edit
       form = UserEditForm(instance=user)
       return render(request, 'gym/user_edit.html', {'form': form})

@login_required
def user_delete(request, username):
    users = User.objects.get(username=username)
    users.delete()
    return redirect('gym:users_list')

@login_required
def user_new(request):
   if request.method == "POST":
       form = UserEditForm(request.POST)
       if form.is_valid():
           newuser = form.save(commit=False)
           newuser.date_joined = timezone.now()
           newuser.save()
           users = User.objects.filter(date_joined__lte=timezone.now())
           return render(request, 'gym/users_list.html',
                         {'users': users})
   else:
       form = UserEditForm()
       # print("Else")
   return render(request, 'gym/user_new.html', {'form': form})


@login_required
def reports_list(request):
    return render(request, 'gym/reports_list.html',
                  {'gym': reports_list})


@login_required
def user_summary_pdf(request):
    users = User.objects.all()
    context = {'users': users,}
    template = get_template('gym/user_summary_pdf.html')
    html = template.render(context)
    pdf = render_to_pdf('gym/user_summary_pdf.html', context)

    return pdf


@login_required
def activities_summary_pdf(request):
    availabilities = Availability.objects.filter(created_date__lte=timezone.now())
    context = {'availabilities': availabilities,}
    template = get_template('gym/activities_summary_pdf.html')
    html = template.render(context)
    pdf = render_to_pdf('gym/activities_summary_pdf.html', context)
    return pdf

def contact(request):
    form_class = ContactForm

    return render(request, 'registration/contact.html', {'form': form_class})


@login_required
def equipment_list(request):
    equipments = GymEquipment.objects.all()
    return render(request, 'gym/equipment_list.html', {'equipments': equipments})



@login_required
def equipment_edit(request, pk):
   equipment = get_object_or_404(GymEquipment, pk=pk)
   if request.method == "POST":
       # update
       form = EquipmentEditForm(request.POST, instance=equipment)
       if form.is_valid():
           equipment = form.save(commit=False)
           equipment.updated_date = timezone.now()
           equipment.save()
           equipments = GymEquipment.objects.filter()
           print(equipments)
           return render(request, 'gym/equipment_list.html',
                         {'equipments': equipments})
   else:
        # edit
       form = EquipmentEditForm(instance=equipment)
       return render(request, 'gym/equipment_edit.html', {'form': form})

@login_required
def equipment_delete(request, pk):
    equipments = get_object_or_404(GymEquipment, pk=pk)
    equipments.delete()
    return redirect('gym:equipment_list')

@login_required
def equipment_new(request):
   if request.method == "POST":
       form = EquipmentEditForm(request.POST)
       if form.is_valid():
           newequipment = form.save(commit=False)
           newequipment.date_joined = timezone.now()
           newequipment.save()
           equipments = GymEquipment.objects.filter()
           return render(request, 'gym/equipment_list.html',
                         {'equipments': equipments})
   else:
       form = EquipmentEditForm()
       # print("Else")
   return render(request, 'gym/equipment_new.html', {'form': form})


@login_required
def CustomerViewEquipments(request):
    equipments = GymEquipment.objects.filter()
    return render(request, 'gym/CustomerViewEquipments.html',
                 {'equipments': equipments})

@login_required
def equipment_summary_pdf(request):
    equipments = GymEquipment.objects.filter()
    context = {'equipments': equipments,}
    template = get_template('gym/equipment_summary_pdf.html')
    html = template.render(context)
    pdf = render_to_pdf('gym/equipment_summary_pdf.html', context)
    return pdf


def About(request):
   return render(request, 'gym/About.html',
                 {'vna': About})
