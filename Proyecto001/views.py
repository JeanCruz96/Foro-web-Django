#se instalo previamente el paquete django porque salia error al importar
from django.http import HttpResponse


# Request: para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP(transferencia de hipertexto)

# esto es una vista
def bienvenido(request):
        # pasamos un objeto de tipo rquest como 1er argumento
    return HttpResponse("<p style='color:blue;'>HOLA JEANCILLO COMO TE HA IDO ESTA SEMANA :)<p>")