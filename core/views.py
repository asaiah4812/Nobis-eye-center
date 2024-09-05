from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Day, Doctor, Book, Message
from .forms import RegisterForm, BookForm, MessageForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    services = Service.objects.all()[0:8]
    doctors = Doctor.objects.all()  
    books = Book.objects.all()
    messages = Message.objects.all()
    
    if request.method == 'POST':
        forms = BookForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('home')
    else:
        forms = BookForm()
        
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = MessageForm()
        

    
    context = {
        'services':services,
        'form':form,
        'messages':messages,
        'doctors':doctors,
        'forms':forms,
        'books':books,
        }
    return render(request, 'core/home.html', context)

def services_detail(request, slug):
    service = get_object_or_404(Service, slug=slug )
    context = {
        'service':service,
        }
    return render(request, 'core/services_detail.html', context)


def doctors(request):
    doctors = Doctor.objects.all()[0:9]
    context = {
        'doctors':doctors
    }
    return render(request, 'core/doctors.html', context)

def book(request):
    book = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book')
    form = BookForm()
    context = {
        'book':book,
        'form':form,
    }
  
    return render(request, 'core/book.html', context)

def about(request):
    context = {}
    return render(request, 'core/about.html', context)

def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)
def sign_up(request):
    if request.method == 'POST':
        form =  RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    context = {
        'form':form
    }
    return render(request, 'registration/sign_up.html', context)

def doctors_detail(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug )
    context = {
       'doctor': doctor 
    }
    return render(request, 'core/doctor_detail.html', context)