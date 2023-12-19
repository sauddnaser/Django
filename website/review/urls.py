from django.urls import path
from .views import ReviewsView
from .views import ShowView

urlpatterns = [
    path('review/', ReviewsView.as_view(), name="reviews"),
    path('showReviews', ShowView.as_view(), name="showReviews"),
]