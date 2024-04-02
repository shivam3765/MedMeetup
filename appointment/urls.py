from django.urls import path
from appointment import views

urlpatterns = [
    path("appoint/", views.appointment, name="appointment"),
]