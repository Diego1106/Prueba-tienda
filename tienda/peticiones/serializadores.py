from  rest_framework import serializers 
from peticiones.models import pqrs
 
 
class TutorialSerializer(serializers.ModelSerializer): 
    class Meta:
        model = pqrs
        fields = ('id',
                  'numero_documento',
                  'nombres_apellidos',
                  'telefono_fijo',
                  'celular',
                  'email',
                  'titulo_pqr',
                  'descripcion_pqr',
                  'estado_pqr',
                  'fecha')

