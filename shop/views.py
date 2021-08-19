from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, ProductSelect
from django.core.paginator import Paginator


# ------ All Products ------


def all_products(request):
    """
    Returns all products
    """
    products = Product.objects.all()

    # from django docs
    paginator = Paginator(products, 12)  # Show 12 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }

    return render(request, 'shop/shop_products.html', context)


def search(request):
    """
    Search page functionality.
    Returns results
    Edited from Boutique Ado Mini Project
    """

    products = Product.objects.all()

    # set default to none to avoid errors
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('search'))

            queries = Q(
                        name__icontains=query) | Q(
                        description__icontains=query
                        )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'shop/search_shop.html', context)


def product_detail(request, product_id):
    """
    Returns specified product
    """
    product = get_object_or_404(Product, pk=product_id)
    product_options = product.product_select.all()

    # gets the product variations to select
    product_select = ProductSelect.objects.filter(
        product_select=product_options,
        product=product)
    product_selected = product_select

    context = {
        'product': product,
        'product_options': product_options,
        'product_selected': product_selected,
    }

    return render(request, 'shop/product.html', context)


# ------ Courses ------


def courses(request):
    """
    Returns All Courses
    """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_category': categories,
    }

    return render(request, 'shop/courses.html', context)


# ------ Apparel ------


def apparel(request):
    """
    Returns All Apparel
    """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_category': categories,
    }

    return render(request, 'shop/apparel.html', context)
