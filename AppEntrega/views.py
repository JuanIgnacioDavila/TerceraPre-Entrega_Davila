from django.shortcuts import render,redirect
from AppEntrega.models import ClienteModel,ProductoModel,TiendaModel
from AppEntrega.forms import ClienteForm,ProductoForm,TiendaForm,BuscarClienteForm,BuscarProductoForm,BuscarTiendaForm

# Create your views here.

def cliente(request):
    allclientes=ClienteModel.objects.all()
    context={
        "clientes":allclientes,
        "clienteform":ClienteForm(),
        "buscarcliente":BuscarClienteForm(),
    }

    if request.method =="POST":
        miForm=ClienteForm(request.POST)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            cliente_save=ClienteModel(
                nombre=informacion['nombre'],
                email=informacion['email'],
                documento=informacion['documento'],
                
            )
            cliente_save.save()
            return redirect("AppEntregaProducto")
    
           
    return render(request,"AppEntrega/cliente.html",context)

def producto(request):
    allproductos=ProductoModel.objects.all()
    context={
        "productos":allproductos,
        "productoform":ProductoForm(),
        "buscarproducto":BuscarProductoForm(),
    }

    if request.method =="POST":
        miForm=ProductoForm(request.POST)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            producto_save=ProductoModel(
                nombre=informacion['nombre'],
                color=informacion['color'],
                tipo=informacion['tipo'],
                codigo=informacion['codigo'],
                descripcion=informacion['descripcion'],
                
            )
            producto_save.save()
            return redirect("AppEntregaTienda")
    
           
    return render(request,"AppEntrega/producto.html",context)

def tienda(request):
    alltiendas=TiendaModel.objects.all()
    context={
        "tiendas":alltiendas,
        "tiendaform":TiendaForm(),
        "buscartienda":BuscarTiendaForm(),
    }

    if request.method =="POST":
        miForm=TiendaForm(request.POST)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            tienda_save=TiendaModel(
                nombre=informacion['nombre'],
                direccion=informacion['direccion'],
                telefono=informacion['telefono'],
                
            )
            tienda_save.save()
            return redirect("AppEntregaRegistro")
    
           
    return render(request,"AppEntrega/tienda.html",context)

def registro(request):
    return render(request,"AppEntrega/registro.html")


def busquedaCliente(request):
    mi_form=BuscarClienteForm(request.GET)
    if mi_form.is_valid():
        informacion=mi_form.cleaned_data
        filtro=ClienteModel.objects.filter(nombre__icontains=informacion['nombre'])
        context={
            "filtro":filtro,
        }

    return render(request,"AppEntrega/resultadoC.html",context)

def busquedaProducto(request):
    mi_form=BuscarProductoForm(request.GET)
    if mi_form.is_valid():
        informacion=mi_form.cleaned_data
        filtro=ProductoModel.objects.filter(nombre__icontains=informacion['nombre'])
        context={
            "filtro":filtro,
        }
    return render(request,"AppEntrega/resultadoP.html",context)

def busquedaTienda(request):
    mi_form=BuscarTiendaForm(request.GET)
    if mi_form.is_valid():
        informacion=mi_form.cleaned_data
        filtro=TiendaModel.objects.filter(nombre__icontains=informacion['nombre'])
        context={
            "filtro":filtro,
        }
    return render(request,"AppEntrega/resultadoT.html",context)


    

    