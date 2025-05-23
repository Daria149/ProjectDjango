from tkinter.font import names

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}, сообщение получено.")
    return render(request, 'contacts.html')
