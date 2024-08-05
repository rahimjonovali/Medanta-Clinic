from django.contrib import admin
from .models import Appointment, ClinicSettings

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'birth_year', 'phone_number', 'appointment_date', 'appointment_time', 'source')
    list_display_links = ('id','full_name', 'birth_year', 'phone_number', 'appointment_date', 'appointment_time', 'source')
    list_filter = ('appointment_date', 'source')
    search_fields = ('full_name', 'phone_number')
@admin.register(ClinicSettings)
class ClinicSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'time_interval','admission_name')
    list_display_links = ('start_time', 'end_time', 'time_interval', 'admission_name')

    def has_add_permission(self, request):
        # Allow creating ClinicSettings only if none exist
        return ClinicSettings.objects.count() == 0

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the ClinicSettings instance
        return False