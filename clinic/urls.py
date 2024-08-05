from django.urls import path, include
from .views import AppointmentCreateView, AppointmentViewSet, MonitorAppointmentsView,AdministrationView, call_patient
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls)),
    path('qabul/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('qabul/success/', AppointmentCreateView.appointment_success, name='appointment_success'),
    path('qabul/monitor/', MonitorAppointmentsView.as_view(), name='monitor_appointments'),
    path('administration/', AdministrationView.as_view(), name='administration'),
    path('administration/call/<int:pk>/', call_patient, name='call_patient'),

]
