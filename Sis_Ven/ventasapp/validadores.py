from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator #para hacer validaciones especiales letras y espacio (o expresiones regulares)
from datetime import timedelta
from datetime import date
def validacion_numeros(value):
    if not value.isdigit():
        raise ValidationError("El valor debe contener solo números") #raise funciona como como un print para devolver un mensajhe en caso de que no se cumpla la condicion
    
def Validacion_letras(value):
    if not value.isalpha():
        raise ValidationError("El valor debe contener solo letras")

 #expresiones regulares
   
validacion_especial = RegexValidator(
    regex= r'^[a-zA-Z\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'

)

#validacion numeros letras y espacios
validacion_especial2 = RegexValidator(
    regex= r'^[a-zA-Z0-9\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'

)

#validacion numeros, letras y espacios y caracteres especiales
validacion_especial3 = RegexValidator(
    regex= r'^[a-zA-Z0-9,-ó\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'
)

def validacion_edad_maxima(fecha_nacimiento):
    edad = (date.today() - fecha_nacimiento).days // 365
    if edad > 60:
        raise ValidationError("La edad máxima para el registro es de 60 años.")

def validacion_fechas_creacion_vencimiento(fecha_creacion, fecha_vencimiento):
    if fecha_creacion == fecha_vencimiento:
        raise ValidationError("La fecha de creación no puede ser igual a la fecha de vencimiento.")
    
def validacion_fecha_vencimiento(fecha_creacion, fecha_vencimiento):
    if fecha_vencimiento > fecha_creacion + timedelta(days=5*365):
        raise ValidationError("La fecha de vencimiento no debe ser mayor a 5 años desde la fecha de creación.")