from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import (
    ClientSerializer, 
    ClientDetailSerializer, 
    ProjectSerializer,
    ProjectListSerializer
)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated] 
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClientDetailSerializer
        return ClientSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer
    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Users data:", request.data.get('users'))
        project = serializer.save()
        response_data = {
            'id': project.id,
            'project_name': project.project_name,
            'client': project.client.client_name,
            'users': [{'id': user.id, 'name': user.username} for user in project.users.all()],
            'created_at': project.created_at,
            'created_by': project.created_by.username
            }
        return Response(response_data, status=status.HTTP_201_CREATED)