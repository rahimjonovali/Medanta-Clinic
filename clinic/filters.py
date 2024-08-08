import django_filters
from .models import Appointment


class AppointmentFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Appointment
        fields = ['full_name']
