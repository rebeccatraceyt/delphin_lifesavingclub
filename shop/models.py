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
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


# ------ Courses ------


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


class AgeRange(models.Model):
    """
    Defines age range for course
     (for filtering purposes)
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


class Course(models.Model):
    """
    Courses model
    """
    product_type = models.ForeignKey('ProductType',
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    lvl_age = models.CharField(max_length=254, default=0)
    age_range = models.ForeignKey('AgeRange',
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL)
    times = models.ManyToManyField(Time,
                                   through='CourseTime',
                                   related_name='course_time')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class CourseTime(models.Model):
    """
    Establishes relationship between Course and Time.
    Counts stock
    """
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='course_times')
    stock_count = models.IntegerField(default=12)

    def __str__(self):
        return str(self.stock_count)


# ------ Apparel ------


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
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sizes = models.ManyToManyField(Size,
                                   through='ApparelSize',
                                   related_name='apparel_size')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ApparelSize(models.Model):
    """
    Establishes relationship between Apparel and Size.
    Counts stock
    ref: https://tinyurl.com/ps257c2r
    """
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    apparel = models.ForeignKey(Apparel,
                                on_delete=models.CASCADE,
                                related_name='apparel_sizes')
    stock_count = models.IntegerField(default=30)

    def __str__(self):
        return str(self.stock_count)
