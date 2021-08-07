from django.urls import re_path

from . import views

urlpatterns = [
    re_path('plan/', views.planView.as_view()),
    re_path('plans/', views.plansView.as_view()),
    re_path('sec/', views.secView.as_view()),
]
