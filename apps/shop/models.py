from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre de la categoria')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    db_table = 'product_category'

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['name']
        verbose_name = 'Categoria de product'
        verbose_name_plural = 'Categorias de productos'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de Producto')
    description = models.TextField(max_length=1000, verbose_name='Descripcion')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    stock_level = models.IntegerField(verbose_name='Nivel de stock')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    image = models.ImageField(upload_to='products/', verbose_name='Imagen')
    created_at = models.DateTimeField(auto_now_add=True)
    db_table = 'product'

    def __str__(self):
        return self.name

    def delete(self):
        self.image.delete(self.image.name)
        super.delete()

    class Meta():
        ordering = ['name']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'