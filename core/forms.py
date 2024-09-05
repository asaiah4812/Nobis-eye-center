from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . models import Book, Message
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    number = forms.CharField( max_length=12,)
    
    class meta:
        model = User
        fields = ['username', 'email', 'number' 'password1', 'password2',]
          

class BookForm(ModelForm):
    name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your name'}))
    number= forms.IntegerField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your number'}))
    email= forms.EmailField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    my_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Book
        fields = ['name', 'number', 'email', 'my_date']


class MessageForm(ModelForm):
    name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your name'}))
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    password= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter password'}))
    class Meta:
        model = Message
        fields = ['name', 'email', 'password', 'msg']
        
