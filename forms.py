
from wtforms import Form
from wtforms import StringField, EmailField, IntegerField
from wtforms import validators

class UsersForm(Form):
    nombre = StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    apaterno = StringField('apaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un apellido valido')
    ])
    amaterno = StringField('amaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un apellido valido')
    ])
    edad = IntegerField('edad',[
        validators.number_range(min=1, max=20, message='Valor no valido')
    ])
    correo = EmailField('correo',[
        validators.Email(message='Ingresa un correo valido')
    ])


    


