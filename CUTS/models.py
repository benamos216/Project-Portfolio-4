from django.db import models

# Create your models here.
class Supplier (models.Model):
    supplier = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.supplier


class Range (models.Model):
    supplier = models.ForeignKey('Supplier', related_name='Supplier', on_delete=models.CASCADE)
    ranges = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.ranges


class Roll (models.Model):
    ranges = models.ForeignKey('Range', on_delete=models.CASCADE, related_name='Range')
    roll_colour = models.CharField(max_length=20, null=False, blank=False)
    roll_width = models.CharField(max_length=2, null=False, blank=False)
    roll_size = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    location = models.CharField(max_length=3, null=False, blank=False)

    def __str__(self):
        return self.rolls