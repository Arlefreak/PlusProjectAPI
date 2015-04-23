from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'clients', views.ClientViewSet)

urlpatterns = [
        url(r'^$', views.api_root, name='api-root'),
        url(r'^', include(router.urls)),
]
