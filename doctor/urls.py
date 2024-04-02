from django.urls import path
from doctor import views

urlpatterns = [
    path("doctor/<id>/", views.doctors, name="doctors"),
    path("department/<id>/", views.department, name="department"),
]