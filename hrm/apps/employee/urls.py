from django.urls import path
from apps.employee import views

urlpatterns = [
    path('clockin/', views.IdentifyUserView.as_view()),
]
