from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ListToDo(generics.ListAPIView): #Read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

class DetailToDo(generics.RetrieveAPIView):  #Update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

class CreateToDo(generics.CreateAPIView):      #Create
    queryset= ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

class DelateToDo(generics.DestroyAPIView):     #Delete
    queryset = ToDo.objects.all()
    serializer_class= ToDoSerializer
    permission_classes = [IsAuthenticated]