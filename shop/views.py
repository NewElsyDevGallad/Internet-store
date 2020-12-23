from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, "shop/index.html")


def paginate(request, obj):
    paginator = Paginator(obj, 3)
    page = request.GET.get('page')
    try:
        prods = paginator.page(page)
    except PageNotAnInteger:
        prods = paginator.page(1)
    except EmptyPage:
        prods = paginator.page(paginator.num_pages)
    return prods, page


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    prods, page = paginate(request, products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        prods, page = paginate(request, products)
    return render(request,
                  'shop/product/list.html',
                  {'page': page,
                   'category': category,
                   'categories': categories,
                   'products': prods})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
