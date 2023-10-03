from django.conf import settings
from django.core.mail import send_mail

from catalog.models import Product
from order.models import Order


def send_order_email(order_item: Order):
    send_mail(
        'Заявка на покупку продукта',
        f'{order_item.name} ({order_item.email}) хочет купить ваш продукт {order_item.product.name}. Вот сообщение: {order_item.message}',
        settings.EMAIL_HOST_USER,
        []
    )
