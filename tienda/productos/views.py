from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, DeleteView

from django.urls import reverse_lazy

from django.db.models import Q, Max, Min
from tienda.productos.models import Producto, CarritoCompras
import conekta

# Create your views here.

class DetalleProducto(DetailView):
    template_name = 'detalle.html'
    model = Producto


class ListadoProducto(ListView):
    template_name = 'listado_productos.html'
    modelo = Producto
    paginate_by = 3

    def get_queryset(self):
        query = None

        if ('nombre' in self.request.GET) and self.request.GET['nombre'] != "":
            query = Q(nombre=self.request.GET["nombre"])

        if ('maximo' in self.request) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(precio__lte=int(float(self.request.GET['maximo'])))
                else:
                    query = query & Q(precio__lte=int(float(self.request.GET['maximo'])))
            except:
                pass

        if ('minimo' in self.request) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(precio__gte=int(float(self.request.GET['minimo'])))
                else:
                    query = query & Q(precio__gte=int(float(self.request.GET['minimo'])))
            except:
                pass

        if query is not None:
            productos = Producto.objects.filter(query)
        else:
            productos = Producto.objects.all()
        return productos

    def get_context_data(self, **kwargs):
        context = super(ListadoProducto, self).get_context_data(**kwargs)
        context['maximo'] = Producto.objects.all().aggregate(Max('precio'))['precio__max']
        context['minimo'] = Producto.objects.all().aggregate(Min('precio'))['precio__min']
        return context


class AniadirCarrito(LoginRequiredMixin, CreateView):
    model = CarritoCompras
    fields = ('usuario', 'producto', 'precio',)
    success_url = reverse_lazy('indice')
    login_url = 'ingresar'


class EliminarCarrito(LoginRequiredMixin,DeleteView):
    queryset = CarritoCompras.objects.filter(comprado=False)
    model = CarritoCompras
    success_url = reverse_lazy('indice')
    login_url = 'ingresar'


class ListarCarrito(LoginRequiredMixin,ListView):
    template_name = 'carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarrito, self).get_context_data(**kwargs)
        context['tab'] = 'sincomprar'
        return context


class ListarCarritoPendientes(LoginRequiredMixin,ListView):
    template_name = 'carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=True)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoPendientes, self).get_context_data(**kwargs)
        context['tab'] = 'pendientes'
        return context


class ListarCarritoFinalizadas(LoginRequiredMixin,ListView):
    template_name = 'carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=True,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoFinalizadas, self).get_context_data(**kwargs)
        context['tab'] = 'finalizadas'
        return context
