from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Especialidad
from .forms import EspecialidadForm
from .models import Paciente
from .forms import PacienteForm
from .models import Medico
from .forms import MedicoForm
from .models import ConsultaMedica
from .forms import ConsultaMedicaForm
from .models import Tratamiento
from .forms import TratamientoForm
from .models import Medicamento
from .forms import MedicamentoForm
from .models import RecetaMedica
from .forms import RecetaMedicaForm
from rest_framework import viewsets
from .serializers import EspecialidadSerializer
from .serializers import PacienteSerializer
from .serializers import MedicoSerializer
from .serializers import ConsultaMedicaSerializer
from .serializers import TratamientoSerializer
from .serializers import MedicamentoSerializer
from .serializers import RecetaMedicaSerializer

"""
Este archivo define las vistas principales de la aplicación médica.

Incluye vistas basadas en funciones (FBV) para realizar las operaciones CRUD
de cada entidad (Especialidad, Paciente, Médico, Consulta, Tratamiento, Medicamento y Receta),
utilizando los formularios y modelos correspondientes.

También contiene los ViewSets del API REST implementados con Django REST Framework,
los cuales permiten exponer los datos de cada modelo a través de endpoints JSON.

"""






def especialidad_list(request):
   
    especialidades = Especialidad.objects.all()
    return render(request, 'gestion/especialidad_list.html', {'especialidades': especialidades})


def especialidad_create(request):
    
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('especialidad_list')
    else:
        form = EspecialidadForm()
    return render(request, 'gestion/especialidad_form.html', {'form': form})


def especialidad_update(request, pk):
   
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('especialidad_list')
    else:
        form = EspecialidadForm(instance=especialidad)
    return render(request, 'gestion/especialidad_form.html', {'form': form})


def especialidad_delete(request, pk):
  
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == 'POST':
        especialidad.delete()
        return redirect('especialidad_list')
    return render(request, 'gestion/especialidad_confirm_delete.html', {'especialidad': especialidad})


def paciente_list(request):
    
    pacientes = Paciente.objects.all()
    return render(request, 'gestion/paciente_list.html', {'pacientes': pacientes})


def paciente_create(request):

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'gestion/paciente_form.html', {'form': form})


def paciente_update(request, pk):

    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'gestion/paciente_form.html', {'form': form})


def paciente_delete(request, pk):

    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    return render(request, 'gestion/paciente_confirm_delete.html', {'paciente': paciente})


def medico_list(request):
    especialidad_id = request.GET.get('especialidad')
    if especialidad_id:
        medicos = Medico.objects.filter(especialidad_id=especialidad_id)
    else:
        medicos = Medico.objects.all()
    especialidades = Especialidad.objects.all()
    return render(request, 'gestion/medico_list.html', {
        'medicos': medicos,
        'especialidades': especialidades,
        'especialidad_id': especialidad_id,})


def medico_create(request):

    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()
    return render(request, 'gestion/medico_form.html', {'form': form})


def medico_update(request, pk):

    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'gestion/medico_form.html', {'form': form})


def medico_delete(request, pk):

    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('medico_list')
    return render(request, 'gestion/medico_confirm_delete.html', {'medico': medico})

def consulta_medica_list(request):
    medico_id = request.GET.get('medico')
    if medico_id:
        consultas = ConsultaMedica.objects.filter(medico_id=medico_id)
    else:
        consultas = ConsultaMedica.objects.all()
    medicos = Medico.objects.all()
    return render(request, 'gestion/consulta_medica_list.html', {
        'consultas': consultas,
        'medicos': medicos,
        'medico_id': medico_id,})


def consulta_medica_create(request):
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_medica_list')
    else:
        form = ConsultaMedicaForm()
    return render(request, 'gestion/consulta_medica_form.html', {'form': form})

def consulta_medica_update(request, pk):

    consulta = get_object_or_404(ConsultaMedica, pk=pk)
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta_medica_list')
    else:
        form = ConsultaMedicaForm(instance=consulta)
    return render(request, 'gestion/consulta_medica_form.html', {'form': form})

def consulta_medica_delete(request, pk):
    
    consulta = get_object_or_404(ConsultaMedica, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta_medica_list')
    return render(request, 'gestion/consulta_medica_confirm_delete.html', {'consulta': consulta})


def tratamiento_list(request):

    tratamientos = Tratamiento.objects.all()
    return render(request, 'gestion/tratamiento_list.html', {'tratamientos': tratamientos})


def tratamiento_create(request):

    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tratamiento_list')
    else:
        form = TratamientoForm()
    return render(request, 'gestion/tratamiento_form.html', {'form': form})


def tratamiento_update(request, pk):
    
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect('tratamiento_list')
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, 'gestion/tratamiento_form.html', {'form': form})


def tratamiento_delete(request, pk):
  
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == 'POST':
        tratamiento.delete()
        return redirect('tratamiento_list')
    return render(request, 'gestion/tratamiento_confirm_delete.html', {'tratamiento': tratamiento})


def medicamento_list(request):
    
    medicamentos = Medicamento.objects.all()
    return render(request, 'gestion/medicamento_list.html', {'medicamentos': medicamentos})


def medicamento_create(request):
    
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamento_list')
    else:
        form = MedicamentoForm()
    return render(request, 'gestion/medicamento_form.html', {'form': form})


def medicamento_update(request, pk):
    
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamento_list')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'gestion/medicamento_form.html', {'form': form})


def medicamento_delete(request, pk):
   
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamento_list')
    return render(request, 'gestion/medicamento_confirm_delete.html', {'medicamento': medicamento})


def receta_medica_list(request):
  
    recetas = RecetaMedica.objects.all()
    return render(request, 'gestion/receta_medica_list.html', {'recetas': recetas})


def receta_medica_create(request):
    
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receta_medica_list')
    else:
        form = RecetaMedicaForm()
    return render(request, 'gestion/receta_medica_form.html', {'form': form})


def receta_medica_update(request, pk):
  
    receta = get_object_or_404(RecetaMedica, pk=pk)
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('receta_medica_list')
    else:
        form = RecetaMedicaForm(instance=receta)
    return render(request, 'gestion/receta_medica_form.html', {'form': form})


def receta_medica_delete(request, pk):
    
    receta = get_object_or_404(RecetaMedica, pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('receta_medica_list')
    return render(request, 'gestion/receta_medica_confirm_delete.html', {'receta': receta})

def menu_principal(request):
    return render(request, 'gestion/menu.html')

"""
---------------
ViewSets de la API REST (Django REST Framework)
---------------
Definen los endpoints REST para consumir los datos de cada modelo.
"""

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer