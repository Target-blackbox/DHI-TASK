from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectListSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client_name', 'created_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    project_name = serializers.CharField(required=True)
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    client_id = serializers.IntegerField(write_only=True)
    users = UserSerializer(many=True, read_only=True)
    client_name = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_id', 'client_name', 'users', 'created_at', 'created_by']
    def get_client_name(self, obj):
        return obj.client.client_name
    def get_created_by(self, obj):
        return obj.created_by.username
    def create(self, validated_data):
        client_id = validated_data.pop('client_id')
        users_data = self.context['request'].data.get('users', [])
        try:
            client = Client.objects.get(id=client_id)
            project = Project.objects.create(
                project_name=validated_data['project_name'],
                client=client,
                created_by=self.context['request'].user
            )
            if isinstance(users_data, list):
                for user_id in users_data:
                    try:
                        user = User.objects.get(id=user_id)
                        project.users.add(user)
                    except User.DoesNotExist:
                        pass 
            return project
        except Client.DoesNotExist:
            raise serializers.ValidationError("Client with this ID does not exist")

class ProjectDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(source='project_name')
    class Meta:
        model = Project
        fields = ['id', 'name']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'created_by']

class ClientDetailSerializer(serializers.ModelSerializer):
    projects = ProjectDetailSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by']