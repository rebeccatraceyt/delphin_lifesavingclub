from django.db import models


# ------ Product Categories ------


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
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


# ------ Course Filters ------


class Time(models.Model):
    """
    Defines course times
    """
    time = models.CharField(max_length=255)
    time_name = models.CharField(max_length=255, default='monday')

    def __str__(self):
        return str(self.time)

    def get_time_name(self):
        return str(self.time_name)


# ------ Apparel Filters ------


class Size(models.Model):
    """
    Defines apparel size
    """
    size = models.CharField(max_length=255)
    size_name = models.CharField(max_length=255, default='small')

    def __str__(self):
        return str(self.size)

    def get_size_name(self):
        return str(self.size_name)


# ------ All Products ------


class Product(models.Model):
    """ Defines all products """

    name = models.CharField(max_length=254)
    description = models.TextField(default='test')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    is_course = models.BooleanField(default=False, null=True, blank=True)
    times = models.ManyToManyField(Time,
                                   through='CourseTime',
                                   related_name='course_time',
                                   blank=True)
    is_apparel = models.BooleanField(default=False, null=True, blank=True)
    sizes = models.ManyToManyField(Size,
                                   through='ApparelSize',
                                   related_name='apparel_size',
                                   blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


# ------ ManyToMany Through Tables ------


class CourseTime(models.Model):
    """
    Establishes relationship between Course and Time.
    Counts stock
    """
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    course = models.ForeignKey(Product,
                               on_delete=models.CASCADE,
                               related_name='course_times')
    stock_count = models.IntegerField(default=12)

    def __str__(self):
        return str(self.stock_count)


class ApparelSize(models.Model):
    """
    Establishes relationship between Apparel and Size.
    Counts stock
    ref: https://tinyurl.com/ps257c2r
    """
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    apparel = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='apparel_sizes')
    stock_count = models.IntegerField(default=30)

    def __str__(self):
        return str(self.stock_count)
