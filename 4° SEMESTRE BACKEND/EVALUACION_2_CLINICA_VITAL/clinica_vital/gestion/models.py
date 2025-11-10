from django.db import models

# Create your models here.
"""
Este archivo define los modelos principales del sistema médico.
Incluye entidades como Especialidad, Médico, Paciente, Consulta, Tratamiento, Medicamento y Receta.

Los modelos siguen una estructura relacional coherente:
- Un médico pertenece a una especialidad.
- Un paciente puede tener múltiples consultas.
- Cada consulta genera posibles tratamientos y recetas asociadas.
- Los medicamentos se gestionan de forma independiente y se asocian a tratamientos mediante recetas.
"""


class Especialidad(models.Model):
    
    nombre = models.CharField(max_length=100) 
    
    descripcion = models.CharField(max_length=250) 

    def __str__(self):
        
        return self.nombre


class Medico(models.Model):

    nombre = models.CharField(max_length=100)
  
    apellido = models.CharField(max_length=100) 

    rut = models.CharField(max_length=12)  

    correo = models.EmailField(max_length=100) 

    telefono = models.CharField(max_length=20) 

    activo = models.BooleanField(default=True) 
    
    especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE)

    def __str__(self):
        
        return f"{self.nombre} {self.apellido}"
    

class Paciente(models.Model):

    TIPO_SANGRE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    tipo_sangre = models.CharField(max_length=3, choices=TIPO_SANGRE_CHOICES)

    rut = models.CharField(max_length=12)
    
    nombre = models.CharField(max_length=100) 
    
    apellido = models.CharField(max_length=100) 
    
    fecha_nacimiento = models.DateField() 
    
    correo = models.EmailField(max_length=100) 
    
    telefono = models.CharField(max_length=20) # 
    
    direccion = models.CharField(max_length=150) 
    
    activo = models.BooleanField(default=True) 

    def __str__(self):
        
        return f"{self.nombre} {self.apellido}"


class ConsultaMedica(models.Model):
    
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE) 

    fecha_consulta = models.DateTimeField() # 
    
    motivo = models.CharField(max_length=200) 

    diagnostico = models.CharField(max_length=200) 

    estado = models.CharField(max_length=50) 

    def __str__(self):
        
        return f"Consulta de {self.paciente.nombre} ({self.fecha_consulta})"


class Tratamiento(models.Model):

    consulta = models.ForeignKey('ConsultaMedica', on_delete=models.CASCADE) 
    
    descripcion = models.CharField(max_length=250) 

    duracion_dias = models.IntegerField() 

    observaciones = models.CharField(max_length=300) 

    def __str__(self):
        
        return f"Tratamiento para consulta {self.consulta.id}"


class Medicamento(models.Model):
    
    nombre = models.CharField(max_length=100) 
    
    laboratorio = models.CharField(max_length=100) 
    
    stock = models.IntegerField() 

    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        
        return self.nombre


class RecetaMedica(models.Model):
    
    tratamiento = models.ForeignKey('Tratamiento', on_delete=models.CASCADE)
    
    medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE) 
    
    dosis = models.CharField(max_length=50) 
    
    frecuencia = models.CharField(max_length=50)
    
    duracion = models.CharField(max_length=50)

    def __str__(self):
        
        return f"Receta de {self.medicamento.nombre} para tratamiento {self.tratamiento.id}"
