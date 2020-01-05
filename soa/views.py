"""
"""
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
#importation of all models
from soa.models import *
from soa.serializers import UserSerializer
# importation of date
import datetime
import json
# return the current time
def currentTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# create user in the database using this view
#@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def user_register(request):
    data = json.loads(request.body)
    data["date_joined"] = currentTime()
    data["last_login"] = currentTime()
    data["password"] = make_password(data.get("password"))
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": serializer.data})    
    return Response({"error": serializer.errors})
