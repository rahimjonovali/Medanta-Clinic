from django.urls import path,include
from .views import AppointmentCreateView, appointment_success,AppointmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointments')


urlpatterns = [
    path('', include(router.urls)),
    path('qabul', AppointmentCreateView.as_view(), name='appointment_create'),
    path('qabul/success/', appointment_success, name='appointment_success'),
]