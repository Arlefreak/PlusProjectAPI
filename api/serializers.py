from django.forms import widgets
from rest_framework import serializers
from api.models import Project, Task, Payment, Client
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #ProjectsOwned = serializers.HyperlinkedRelatedField(many=True,view_name='project-detail', read_only=True)
    #TasksOwned = serializers.HyperlinkedRelatedField(many=True,view_name='task-detail', read_only=True)
    #PaymentsOwned = serializers.HyperlinkedRelatedField(many=True,view_name='payment-detail', read_only=True)
    #ClientsOwned = serializers.HyperlinkedRelatedField(many=True,view_name='client-detail', read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            #'ProjectsOwned',
            #'TasksOwned',
            #'PaymentsOwned',
            #'ClientsOwned'
        )

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #TaskProjects = serializers.HyperlinkedRelatedField(many=True,view_name='task-detail', read_only=True)
    #PaymentProjects = serializers.HyperlinkedRelatedField(many=True,view_name='payment-detail', read_only=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'owner',
            'name',
            'description',
            'image',
            'status',
            'client',
            #'TaskProjects',
            #'PaymentProjects'
        )

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = (
            'id',
            'owner',
            'name',
            'status',
            'date',
            'dateAdded',
            'project'
        )

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Payment
        fields = (
            'id',
            'owner',
            'name',
            'money',
            'paymentType',
            'date',
            'dateAdded',
            'taxPercentage',
            'project'
        )

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #ProjectsClient = serializers.HyperlinkedRelatedField(many=True,view_name='project-detail', read_only=True)

    class Meta:
        model = Client
        fields = (
            'id',
            'owner',
            'name',
            'email',
            'phone',
            'image',
            #'ProjectsClient'
        )
