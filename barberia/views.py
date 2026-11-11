from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages 
from .models import Cliente, Servicio
from .conexion import barberos as coleccion_barberos

def inicio(request):
    return render(request, 'barberia/inicio.html')

def servicios(request):
    return render(request, 'barberia/servicios.html')

def base(request):
    return render(request, 'barberia/base.html')


def clientes(request):
    if request.method == 'POST':
        nombre_form = request.POST.get('username')  
        correo_form = request.POST.get('email')     
        telefono_form = request.POST.get('telefono') 

        if nombre_form:
            Cliente.objects.create(
                nombre=nombre_form,
                email=correo_form,
                telefono=telefono_form
            )
            return redirect('inicio')

    return render(request, 'barberia/clientes.html')


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.email = request.POST.get('correo')
        cliente.telefono = request.POST.get('telefono')
        cliente.save()
        return redirect('clientes')
    return render(request, 'barberia/editar_cliente.html', {'cliente': cliente})


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'barberia/eliminar_cliente.html', {'cliente': cliente})


def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('username')
        print(f"Intento de login: {correo}")
    return render(request, 'barberia/login.html')


def administrar_servicios(request):
    if request.method == 'POST':
        # Capturamos todos los campos enviados desde la plantilla HTML
        nombre_form = request.POST.get('nombre')
        descripcion_form = request.POST.get('descripcion')  # Trae el tipo de servicio seleccionado
        fecha_form = request.POST.get('fecha')              # Trae la fecha del calendario
        barbero_form = request.POST.get('barbero')          # Trae el barbero elegido

        try:
            # Crea y guarda el nuevo registro en la base de datos
            Servicio.objects.create(
                UK_servicios_nombre=nombre_form,
                descripcion=descripcion_form,
                fecha=fecha_form,
                barbero=barbero_form
            )
            messages.success(request, "¡Servicio reservado con éxito!")
        except Exception as e:
            messages.error(request, f"Error al procesar la reserva: {e}")
            
        return redirect('administrar_servicios')

    # Obtenemos todos los servicios/reservas registrados para listar en la tabla
    todos_los_servicios = Servicio.objects.all()
    
    # Obtenemos la lista de barberos desde MongoDB
    lista_barberos = list(coleccion_barberos.find({}))

    return render(
        request, 
        'barberia/administrar_servicios.html', 
        {
            'servicios': todos_los_servicios,
            'barberos': lista_barberos
        }
    )


def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, PK_idServicio=id)

    if request.method == 'POST':
        servicio.UK_servicios_nombre = request.POST.get('nombre')
        servicio.descripcion = request.POST.get('descripcion')
        servicio.fecha = request.POST.get('fecha')
        servicio.barbero = request.POST.get('barbero')
        servicio.save()
        messages.success(request, "¡Servicio actualizado correctamente!")
        return redirect('administrar_servicios')

    return render(request, 'barberia/editar_servicio.html', {'servicio': servicio})


def eliminar_servicio(request, id):
    if request.method == 'POST':
        servicio = get_object_or_404(Servicio, PK_idServicio=id)
        servicio.delete()
        messages.success(request, "Servicio eliminado de la base de datos.")
    return redirect('administrar_servicios')


def barberos(request):
    lista = list(coleccion_barberos.find({"disponible": True}))
    total_disponibles = len(lista)

    return render(
        request,
        'barberia/barberos.html',
        {
            'barberos': lista,
            'total_disponibles': total_disponibles
        }
    )


def contactos(request):
    return render(request, 'barberia/contactos.html')