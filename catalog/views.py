from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog/products.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    products_item = Product.objects.get(pk=pk)
    products_list = Product.objects.filter(id=pk)
    context = {
        'object_list': products_list,
        'title': f'Продукт - {products_item.name}'
    }
    return render(request, 'catalog/product.html', context)
