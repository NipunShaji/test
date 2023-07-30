from django.shortcuts import render
from django.contrib.auth.views import LoginView

from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
import face_recognition
from apps.employee.models import Employee, Timelog
from django.core.files.images import ImageFile
from django.core.files import File
from datetime import datetime
from rest_framework import status


class IdentifyUserView(TemplateView):
    template_name = "identify-user.html"


class VerifyView(APIView):

    def post(self, request):
        print(request.data)
        image = File(request.data.get('image'), 'unknown.jpeg')
        unknown = face_recognition.load_image_file(image)
        features = face_recognition.face_encodings(unknown)[0]
        query = Employee.objects.all()
        for employee in query:
            
            import pdb
            # pdb.set_trace()
            known = face_recognition.load_image_file(employee.image)
            known_features = face_recognition.face_encodings(known)[0]
            result = face_recognition.compare_faces([known_features], features)
            if result and result[0]:
                Timelog.objects.create(
                    user=employee.user,
                    image=image
                )
                return Response({
                    "first_name": employee.user.first_name,
                    "last_name": employee.user.last_name,
                    "time": datetime.now(),
                    "id": employee.id
                }, content_type="application/json")
        return Response({}, status=status.HTTP_404_NOT_FOUND)
