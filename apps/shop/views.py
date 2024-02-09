from django.shortcuts import get_object_or_404
from .models import Product, Category
from django.views.generic import ListView
from django.db.models import Max

class ListProducts(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'categories'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener todos los productos
        products = Product.objects.all()

        # Obtener mediante GET la categoria y precios del formulario
        category = self.request.GET.get('category', None)
        precio_min = self.request.GET.get('precio_min', None)
        precio_max = self.request.GET.get('precio_max', None)

        # Salvar valor precio_máximo si no se proporciona
        if not precio_min:
            precio_min = 1
            
        # Obtener precio máximo de todos los productos, si no se proporciona    
        if not precio_max:
            precio_max = products.aggregate(Max('price'))['price__max']

        # Filtrar los productos por precio
        products = products.filter(price__range=(precio_min, precio_max))

        # Si existe la categoria, filtro los productos y envio el nombre de la categoria seleccionada
        if category is not None:
            if category != '0':
                products = products.filter(category=category)
                categoria_seleccionada = category
                context['categoria_seleccionada'] = get_object_or_404(Category, id=categoria_seleccionada)

        # Todos los productos por default, filtrados si existe categoria    
        context['products'] = products
        return context