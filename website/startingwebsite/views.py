from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tea

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def chai(request):
    Tea_objects = Tea.objects.all()
    return render(request, 'shop.html', {'Tea_objects': Tea_objects})

class HomeView(ListView):
    model = Tea
    template_name = 'home.html'

class ShopView(ListView):
    model = Tea
    template_name = 'shop.html'

class DetailsView(ListView):
    model = Tea
    template_name = 'details.html'

class ItemsDetails(DetailView):
    model = Tea
    template_name = 'details.html'

class CheckoutView(ListView):
    model = Tea
    template_name = 'checkout.html'


