from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES= [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ]


class SignUpForm(UserCreationForm):
    
  profile_PIC = forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'type':'file', 
      'id' : 'files',  
      'multiple': True
    }))
  
  Category= forms.CharField(label='What is your are?', widget=forms.RadioSelect(choices=CHOICES))

  address = forms.CharField(max_length=500,
    widget=forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  city = forms.CharField(max_length=500,
      widget=forms.TextInput(attrs={
        'type' :'text',
        'class':'form-control',
        'id'   :'title'
      }))

  state = forms.CharField(max_length=500,
      widget=forms.TextInput(attrs={
        'type' :'text',
        'class':'form-control',
        'id'   :'title'
      }))


  pincode = forms.CharField(max_length=500,
      widget=forms.TextInput(attrs={
        'type' :'text',
        'class':'form-control',
        'id'   :'title'
      }))

  class Meta:
    model = User
    fields = ('username','email','first_name','last_name', 'profile_PIC', 'Category', 'address','city','state','pincode','password1', 'password2', )
