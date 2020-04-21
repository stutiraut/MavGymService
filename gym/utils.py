from datetime import datetime, timedelta
from calendar import HTMLCalendar

from django.contrib.auth.models import User
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Availability , Staff
from django.urls import reverse
from xhtml2pdf import pisa


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None,id=None):
		self.year = year
		self.month = month
		self.id=id
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_date__day=day)
		d = ''
		for event in events_per_day:
			url = reverse ( 'gym:event_delete' , args=(event.pk ,) )
			d += f'{event.get_html_url}' \
				 f'<a  href="{url}" onclick="return confirm(\'Are you sure you want to delete?\')">' \
				 f' <i class="fa fa-trash"></i> </a>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul style=\"margin:top:50px; font-size:25px;\"> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):

		events = Availability.objects.filter(start_date__year=self.year, start_date__month=self.month,availability_staff_name_id=self.id)

		cal = f'<table cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal

class CustomerCalendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(CustomerCalendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_date__day=day)
		d = ''
		for event in events_per_day:
			url = reverse ( 'gym:event_delete' , args=(event.pk ,) )
			staff = Staff.objects.get ( id=event.availability_staff_name_id )
			user = User.objects.get ( pk=staff.staff_name_id )
			d += f'<label>{event.activity}</label><br/>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul style=\"margin:top:50px; font-size:15px;\"> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):

		events = Availability.objects.filter(start_date__year=self.year, start_date__month=self.month)

		cal = f'<table cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.replace(u'\ufeff', '').encode("latin-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
