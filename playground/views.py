from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# this is where we define our views/view functions
def calculate():
    x = 1
    y = 2
    return x
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name':'Mosh'})