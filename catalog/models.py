from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='цена')
    date_created = models.DateField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания')
    date_updated = models.DateField(auto_now_add=True, **NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукт'
