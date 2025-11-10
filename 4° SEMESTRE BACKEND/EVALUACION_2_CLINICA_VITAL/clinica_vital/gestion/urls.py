from django.urls import path, include
from rest_framework import routers
from . import views
from .views import (
    EspecialidadViewSet,
    PacienteViewSet,
    MedicoViewSet,
    ConsultaMedicaViewSet,
    TratamientoViewSet,
    MedicamentoViewSet,
    RecetaMedicaViewSet,
)
"""
Configuración del router de Django REST Framework 
para exponer los endpoints de la API de cada modelo.
"""

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'consultas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetas', RecetaMedicaViewSet)

"""
Definición de todas las rutas de la aplicación gestion:
Incluye rutas para menús y vistas CRUD de:
- Especialidad
- Paciente
- Médico
- Consulta Médica
- Tratamiento
- Medicamento
- Receta Médica
Agrupa rutas API y rutas de interfaz clásica.
"""

urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.menu_principal, name='menu_principal'),
    
    path('especialidades/', views.especialidad_list, name='especialidad_list'),
    
    path('especialidades/nueva/', views.especialidad_create, name='especialidad_create'),
    
    path('especialidades/<int:pk>/editar/', views.especialidad_update, name='especialidad_update'),
    
    path('especialidades/<int:pk>/eliminar/', views.especialidad_delete, name='especialidad_delete'),

    
    path('pacientes/', views.paciente_list, name='paciente_list'),

    path('pacientes/nuevo/', views.paciente_create, name='paciente_create'),

    path('pacientes/<int:pk>/editar/', views.paciente_update, name='paciente_update'),
    
    path('pacientes/<int:pk>/eliminar/', views.paciente_delete, name='paciente_delete'),

    
    path('medicos/', views.medico_list, name='medico_list'),

    path('medicos/nuevo/', views.medico_create, name='medico_create')
    ,
    path('medicos/<int:pk>/editar/', views.medico_update, name='medico_update'),

    path('medicos/<int:pk>/eliminar/', views.medico_delete, name='medico_delete'),

    
    path('consultas/', views.consulta_medica_list, name='consulta_medica_list'),
    
    path('consultas/nueva/', views.consulta_medica_create, name='consulta_medica_create'),
    
    path('consultas/<int:pk>/editar/', views.consulta_medica_update, name='consulta_medica_update'),
    
    path('consultas/<int:pk>/eliminar/', views.consulta_medica_delete, name='consulta_medica_delete'),

    

    
    path('tratamientos/', views.tratamiento_list, name='tratamiento_list'),
    
    path('tratamientos/nuevo/', views.tratamiento_create, name='tratamiento_create'),
    
    path('tratamientos/<int:pk>/editar/', views.tratamiento_update, name='tratamiento_update'),
    
    path('tratamientos/<int:pk>/eliminar/', views.tratamiento_delete, name='tratamiento_delete'),

    

    
    path('medicamentos/', views.medicamento_list, name='medicamento_list'),
    
    path('medicamentos/nuevo/', views.medicamento_create, name='medicamento_create'),
    
    path('medicamentos/<int:pk>/editar/', views.medicamento_update, name='medicamento_update'),
    
    path('medicamentos/<int:pk>/eliminar/', views.medicamento_delete, name='medicamento_delete'),

    

    
    path('recetas/', views.receta_medica_list, name='receta_medica_list'),
    
    path('recetas/nueva/', views.receta_medica_create, name='receta_medica_create'),
    
    path('recetas/<int:pk>/editar/', views.receta_medica_update, name='receta_medica_update'),
    
    path('recetas/<int:pk>/eliminar/', views.receta_medica_delete, name='receta_medica_delete'),]

