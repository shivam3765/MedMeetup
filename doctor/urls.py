from django.urls import path
from doctor import views

urlpatterns = [
    path("doctor", views.doctors, name="doctors"),
]