from django.urls import path
from apps.employee import views

urlpatterns = [
    path('clockin/', views.IdentifyUserView.as_view()),
    path('clockin/verify/', views.VerifyView.as_view()),
]
