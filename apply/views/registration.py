# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from jdatetime import date, datetime as dt
# from rest_framework.response import Response
# from datetime import datetime
#
# from accounts.models import Student
# from college.models import Term
# from apply.models import Registration
# from apply.serializer import RegistrationSerializer
#
#
# class RegistrationView(viewsets.ModelViewSet):
#     queryset = Registration.objects.all()
#     serializer_class = RegistrationSerializer
#     permission_classes = [IsAuthenticated]
#
#     def create(self, request, *args, **kwargs):
#         if request.user == Student.objects.get(pk=kwargs.get('pk')):
#             if dt.now() < Term.objects.all().last().selected_start_time and dt.now() > Term.objects.all().last().selected_end_time:
#                 return Response({'message': 'you cant access registeration before that start time'}, status=403)
