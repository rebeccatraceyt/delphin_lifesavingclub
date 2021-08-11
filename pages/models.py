from django.db import models


# ------ Swim Categories  ------


class SwimCategory(models.Model):
    """
    Defines category of swimming programme
     (for filtering purposes)
    """

    class Meta:
        verbose_name_plural = 'Swim Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


# ------ Swim Programme  ------


class SwimProgramme(models.Model):
    """
    Defines Learn To Swim Programme outline
    """

    class Meta:
        verbose_name_plural = 'Swim Programme'

    name = models.CharField(max_length=254)
    description = models.TextField()
    age = models.CharField(max_length=254)
    swim_category = models.ForeignKey('SwimCategory',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.description)
