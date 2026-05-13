from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Venta
from .forms import ProductoForm, VentaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    productos = Producto.objects.all()
    ventas = Venta.objects.all()

    total_productos = productos.count()
    stock_bajo = productos.filter(cantidad__lte=5).count()

    ganancias = 0

    for venta in ventas:
        ganancias += venta.total()

    context = {
        'total_productos': total_productos,
        'stock_bajo': stock_bajo,
        'ganancias': ganancias
    }

    return render(request, 'inventario/dashboard.html', context)


@login_required
def productos(request):

    query = request.GET.get('q')

    productos = Producto.objects.all().order_by('-id')

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query)
        )

    # PAGINADOR
    paginator = Paginator(productos, 10)

    page = request.GET.get('page')

    productos = paginator.get_page(page)

    return render(request,
                  'inventario/productos.html',
                  {
                      'productos': productos
                  })


@login_required
def crear_producto(request):

    if request.method == 'POST':

        form = ProductoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

            return redirect('productos')

    else:
        form = ProductoForm()

    return render(
        request,
        'inventario/producto_form.html',
        {
            'form': form
        }
    )


@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    form = ProductoForm(
        request.POST or None,
        request.FILES or None,
        instance=producto
    )

    if form.is_valid():
        form.save()
        return redirect('productos')

    return render(request, 'inventario/producto_form.html', {
        'form': form
    })


@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()

    return redirect('productos')


@login_required
def ventas(request):
    form = VentaForm(request.POST or None)

    if form.is_valid():
        venta = form.save()

        producto = venta.producto
        producto.cantidad -= venta.cantidad
        producto.save()

        return redirect('ventas')

    ventas = Venta.objects.all().order_by('-fecha')

    return render(request, 'inventario/ventas.html', {
        'form': form,
        'ventas': ventas
    })