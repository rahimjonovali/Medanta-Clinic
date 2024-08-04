from django.shortcuts import render, redirect
from django.views import View
from .forms import AppointmentForm
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentCreateView(View):
    def get(self, request):
        form = AppointmentForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
        return render(request, 'register.html', {'form': form})

def appointment_success(request):
    return render(request, 'success.html')