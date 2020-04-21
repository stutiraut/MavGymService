from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Availability, GymEquipment

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','password1','password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

class EventForm(forms.ModelForm):
  class Meta:
    model = Availability
    widgets = {
      'start_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    }
    fields = ['activity','time','location','start_date']

  def __init__ ( self , *args , **kwargs ) :
      super ( EventForm , self ).__init__ ( *args , **kwargs )
      self.fields['start_date'].widget = DateInput()

class EventEditForm(forms.ModelForm):
  class Meta:
    model = Availability
    widgets = {
      'start_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    }
    fields = ['activity','time','location','start_date']

  def __init__ ( self , *args , **kwargs ) :
      super ( EventEditForm , self ).__init__ ( *args , **kwargs )
      self.fields['start_date'].widget = DateInput()
      self.fields['start_date'].disabled = True

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Subject = forms.CharField(required=False)
    Message = forms.CharField(
    required=True,
    widget=forms.Textarea)

class EquipmentEditForm(forms.ModelForm):
    class Meta:
        model = GymEquipment
        fields = ('name', 'description', 'weight')
