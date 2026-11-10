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
        nombre_form = request.POST.get('nombre')
        descripcion_form = request.POST.get('descripcion')
        precio_form = request.POST.get('precio')
        duracion_form = request.POST.get('duracion')

        try:
            Servicio.objects.create(
                UK_servicios_nombre=nombre_form,
                descripcion=descripcion_form,
                precio=precio_form,
                duracion=duracion_form
            )
            messages.success(request, "¡Servicio registrado con éxito!")
        except Exception as e:
            messages.error(request, f"Error al registrar: {e}")
            
        return redirect('administrar_servicios')


    todos_los_servicios = Servicio.objects.all()
    
    return render(request, 'barberia/administrar_servicios.html', {'servicios': todos_los_servicios})


def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, PK_idServicio=id)

    if request.method == 'POST':
        servicio.UK_servicios_nombre = request.POST.get('nombre')
        servicio.descripcion = request.POST.get('descripcion')
        servicio.precio = request.POST.get('precio')
        servicio.duracion = request.POST.get('duracion')
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