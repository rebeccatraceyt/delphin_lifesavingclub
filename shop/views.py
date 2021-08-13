from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
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
    course_times = product.times.all()
    apparel_sizes = product.sizes.all()

    context = {
        'product': product,
        'course_times': course_times,
        'apparel_sizes': apparel_sizes,
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
