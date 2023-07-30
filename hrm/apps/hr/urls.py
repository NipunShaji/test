from django.urls import path
from apps.hr import views

urlpatterns = [
    path('login/', views.HRLoginView.as_view()),
]