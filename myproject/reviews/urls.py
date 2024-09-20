from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name = "home"),
    path('rform/', views.review_form, name = "review_form"),
]