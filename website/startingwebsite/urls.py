from django.urls import path
from . import views
from .views import HomeView, ShopView, DetailsView, ItemsDetails, CheckoutView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('shop', ShopView.as_view(), name="shop"),
    path('details', DetailsView.as_view(), name="details"),
    path('details<int:pk>', ItemsDetails.as_view(), name="Items-Details"),
    path('checkout', CheckoutView.as_view(), name="checkout"),
]