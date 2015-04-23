from api.models import *
from api.serializers import *
from django.contrib.auth.models import User
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format),
        'payments': reverse('payment-list', request=request, format=format),
        'clients': reverse('client-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given project,
        by filtering against a `project` query parameter in the URL.
        """
        queryset = Project.objects.all()
        user = self.request.user
        client = self.request.QUERY_PARAMS.get('client', None)
        if user.is_anonymous():
            queryset = Project.objects.none()
        else:
            if client is not None:
                queryset = queryset.filter(client__id=client,owner=user)
            else:
                queryset = queryset.filter(owner=user)
        return queryset

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Task.objects.all()
        user = self.request.user
        project = self.request.QUERY_PARAMS.get('project', None)
        if user.is_anonymous():
            queryset = Task.objects.none()
        else:
            if project is not None:
                queryset = queryset.filter(project__id=project,owner=user)
            else:
                queryset = queryset.filter(owner=user)
        return queryset

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Payment.objects.all()
        user = self.request.user
        project = self.request.QUERY_PARAMS.get('project', None)
        if user.is_anonymous():
            queryset = Payment.objects.none()
        else:
            if project is not None:
                queryset = queryset.filter(project__id=project,owner=user)
            else:
                queryset = queryset.filter(owner=user)
        return queryset

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the Clients
        for the currently authenticated user.
        """
        user = self.request.user
        if user.is_anonymous():
            return Client.objects.none()
        else:
            return Client.objects.filter(owner=user)
