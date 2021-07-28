from django.db import models

# ------ Product Types ------


class ProductType(models.Model):
    """
    Defines the product type
     (Apparel or Course)
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# ------ Courses ------


class Time(models.Model):
    """
    Defines course times
    """
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.time


class AgeRange(models.Model):
    """
    Defines age range for course
     (for filtering purposes)
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Course(models.Model):
    """
    Courses model
    """
    product_type = models.ForeignKey('ProductType',
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    age_range = models.ForeignKey('AgeRange',
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL)
    time = models.ManyToManyField(Time, through='CourseTime')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class CourseTime(models.Model):
    """
    Establishes relationship between Course and Time.
    Counts stock
    """
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stock_count = models.IntegerField(default=12)

    def __str__(self):
        return self.stock_count


# ------ Apparel ------


class Size(models.Model):
    """
    Defines course times
    """
    size = models.CharField(max_length=255)

    def __str__(self):
        return self.size


class Category(models.Model):
    """
    Defines size of selected product
     (for filtering purposes)
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Apparel(models.Model):
    """
    Apparel model
    """

    class Meta:
        verbose_name_plural = 'Apparel'

    product_type = models.ForeignKey('ProductType',
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.ManyToManyField(Size, through='ApparelSize')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ApparelSize(models.Model):
    """
    Establishes relationship between Apparel and Size.
    Counts stock
    """
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    apparel = models.ForeignKey(Apparel, on_delete=models.CASCADE)
    stock_count = models.IntegerField(default=12)

    def __str__(self):
        return self.stock_count
