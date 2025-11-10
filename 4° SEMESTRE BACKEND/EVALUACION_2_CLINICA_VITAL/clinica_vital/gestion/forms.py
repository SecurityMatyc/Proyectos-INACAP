from django import forms
from .models import Especialidad
from .models import Paciente
from .models import Medico
from .models import ConsultaMedica
from .models import Tratamiento
from .models import Medicamento
from .models import RecetaMedica

"""
Este archivo define los formularios basados en modelos (ModelForm) para la aplicación médica.

Cada clase de formulario se asocia directamente con un modelo del sistema (Especialidad, Paciente, Medico, etc.),
permitiendo crear, editar y validar datos desde la interfaz de usuario o el panel de administración
de manera automática y coherente con las definiciones del modelo.

"""


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion']
    

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut','nombre', 'apellido', 'fecha_nacimiento', 'tipo_sangre','correo', 'telefono','direccion', 'telefono', 'activo']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            'nombre', 'apellido', 'rut', 'correo', 'telefono', 'activo', 'especialidad']
        
class ConsultaMedicaForm(forms.ModelForm):
    class Meta:
        model = ConsultaMedica
        fields = [
            'paciente', 'medico', 'fecha_consulta', 
            'motivo', 'diagnostico', 'estado']
        
class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = [
            'consulta', 'descripcion', 'duracion_dias', 'observaciones']
        

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            'nombre',
            'laboratorio',
            'stock',
            'precio_unitario']
        
class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = [
            'tratamiento',  
            'medicamento',   
            'dosis',           
            'frecuencia',      
            'duracion']