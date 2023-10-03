from django.db import models


class Order(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='Продукт')

    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(max_length=150,verbose_name='Почта')
    message = models.TextField()

    closed = models.BooleanField(default=False, verbose_name='Заказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} от {self.email}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

