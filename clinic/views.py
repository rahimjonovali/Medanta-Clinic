from django.shortcuts import render, redirect
from django.views import View
from .forms import AppointmentForm
from rest_framework import viewsets
from .models import Appointment, ClinicSettings
from .serializers import AppointmentSerializer
from django.views.generic import ListView
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentCreateView(View):
    def get_admission_name(self):
        clinic_settings = ClinicSettings.objects.first()
        return clinic_settings.admission_name if clinic_settings else "Clinic Appointment"

    def get(self, request):
        form = AppointmentForm()
        admission_name = self.get_admission_name()
        return render(request, 'register.html', {'form': form, 'admission_name': admission_name})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
        admission_name = self.get_admission_name()
        return render(request, 'register.html', {'form': form, 'admission_name': admission_name})

    def appointment_success(request):
        return render(request, 'success.html')


class MonitorAppointmentsView(ListView):
    model = Appointment
    template_name = 'monitor.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        today = timezone.now().date()
        return Appointment.objects.filter(appointment_date=today).order_by('appointment_time')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['today'] = timezone.now().date()
    #     return context
    #

class AdministrationView(ListView):
    model = Appointment
    template_name = 'administration.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.all().order_by('appointment_date', 'appointment_time')


def call_patient(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.called = True
    appointment.save()
    return redirect('administration')
