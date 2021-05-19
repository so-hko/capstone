from django.shortcuts import render
from django.http import HttpResponse
from .models import medicine

def mname(request):
    medicines = medicine.objects
    print(medicine.name)
    return render(request, 'mname.html', {'medicines' : medicines})

def main(request):
    medicines = medicine.objects
    return render(request, 'main.html', {'medicines': medicines})

def mname_file(request):
    medicines = medicine.objects
    return medicines
