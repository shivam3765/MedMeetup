from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.show_appointment, name="profile"),
    path('upload_profile_image/', views.upload_profile_image, name='upload_profile_image'),
]