from django.db import models


# ------ Product Categories ------


class Category(models.Model):
    """
    Defines category of selected product
     (for filtering purposes)
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


# ------ Product Filters ------


class ProductOption(models.Model):
    """
    Defines options available for each product:
    course times and apparel sizes
    """
    product_option = models.CharField(max_length=255)
    option_name = models.CharField(max_length=255, default='monday')

    def __str__(self):
        return str(self.product_option)

    def get_time_name(self):
        return str(self.option_name)


# ------ All Products ------


class Product(models.Model):
    """ Defines all products """

    name = models.CharField(max_length=254)
    description = models.TextField(
        default='A brief description of the product')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_course = models.BooleanField(default=False, blank=False)
    is_apparel = models.BooleanField(default=False, blank=False)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    product_select = models.ManyToManyField(ProductOption,
                                            through='ProductSelect',
                                            related_name='product_options',
                                            blank=True)
    course_info = models.TextField(default='N/A', blank=False)
    course_age = models.CharField(max_length=255, default='10 years')
    image = models.ImageField(null=True, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Products sorted by name
        ref: https://tinyurl.com/3v38mtn5
        """
        ordering = ['name']

    def __str__(self):
        return str(self.name)


# ------ ManyToMany Through Table ------


class ProductSelect(models.Model):
    """
    Establishes relationship between Product and Product Options.
    Counts stock
    """
    product_select = models.ForeignKey(ProductOption,
                                       on_delete=models.CASCADE,
                                       related_name='product_selected')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product_options')
    stock_count = models.IntegerField(default=30)

    def __str__(self):
        return str(self.product_select)

    def get_product(self):
        return str(self.product)
