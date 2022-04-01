from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from reservation import views

urlpatterns = [
    path('', views.ReservationList.as_view()),
]
