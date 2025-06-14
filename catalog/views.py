from tkinter.font import names

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from catalog.models import Product


# def home(request):
#     return render(request, "home.html")



def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}, сообщение получено.")
    return render(request, "contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

