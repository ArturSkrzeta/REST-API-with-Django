from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
# from django.http import HttpResponse

# def main(request):
#        return HttpResponse("<h1>Hello World</h1>")

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
