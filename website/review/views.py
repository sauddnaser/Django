from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Rev
from .forms import ReviewsForm
from django.urls import reverse_lazy

def chai(request):
    Rev_objects = Rev.objects.all()
    return render(request, 'showReviews.html', {'Rev_objects': Rev_objects})

class ReviewsView(CreateView):
    model = Rev
    form_class = ReviewsForm
    template_name = 'reviews.html'
    success_url = reverse_lazy('showReviews')

class ShowView(ListView):
    model = Rev
    template_name = 'showReviews.html'