from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, ProductSelect
from django.core.paginator import Paginator
from .forms import ProductForm


# ------ All Products ------


def all_products(request):
    """
    Returns all products
    """
    products = Product.objects.filter(approved=True)

    # from django docs
    paginator = Paginator(products, 12)  # Show 12 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'from_shop': True,
    }

    return render(request, 'shop/shop_products.html', context)


def search(request):
    """
    Search page functionality.
    Returns results
    Edited from Boutique Ado Mini Project
    """

    products = Product.objects.filter(approved=True)

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

    if not request.user.is_superuser:
        if product.approved:
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
    
        else:
            messages.error(request, 'Sorry, this product does not exist yet')
            return redirect(reverse('home'))
    
    else:
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

    products = Product.objects.filter(approved=True)
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_category': categories,
        'from_courses': True,
    }

    return render(request, 'shop/courses.html', context)


# ------ Apparel ------


def apparel(request):
    """
    Returns All Apparel
    """

    products = Product.objects.filter(approved=True)
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_category': categories,
        'from_apparel': True,
    }

    return render(request, 'shop/apparel.html', context)


# ------ Admin ------

@login_required
def product_management(request):
    """
    Manage products in the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do that')
        return redirect(reverse('home'))

    to_be_approved = Product.objects.filter(approved=False)

    template = 'shop/product_management.html'
    context = {
        'to_be_approved': to_be_approved,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product \
                Please ensure all fields are valid')
    else:
        # ensures form errors aren't wiped out
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    # get the product
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # instantiate form with specified instance being product chosen
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure all fields are vaild')
    else:
        # instantiating the product form (using the product)
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'editing': True,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    # get product (or 404)
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted!')
    return redirect(reverse('all_products'))
