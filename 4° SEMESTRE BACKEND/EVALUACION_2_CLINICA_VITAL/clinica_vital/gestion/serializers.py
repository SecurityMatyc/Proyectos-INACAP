from rest_framework import serializers
from .models import Especialidad
from .models import Paciente
from .models import Medico
from .models import ConsultaMedica
from .models import Tratamiento
from .models import Medicamento
from .models import RecetaMedica

"""
Este archivo define los serializers del proyecto.

Los serializers convierten las instancias de los modelos en formatos fácilmente intercambiables,
como JSON o XML, y viceversa. Esto permite que los datos del sistema puedan ser consumidos
por aplicaciones externas a través de la API REST.

Cada clase de serializer está asociada directamente a un modelo y utiliza 'fields = "__all__"'
para incluir todos los campos del modelo en la serialización.

"""


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class RecetaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaMedica
        fields = '__all__'