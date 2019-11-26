from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length = 20)


class Laptop(models.Model):
    name = models.CharField(max_length = 30)
    price = models.CharField(max_length = 30)


class Graphic(models. Model):
    name = models.TextField(default='')
    programs = models.ManyToManyField(Program, related_name='graphics', blank=True)
    laptops = models.ManyToManyField(Laptop, related_name='graphics', blank=True)

    def __str__(self):
        return self.name


# class Info(models.Model):
#     laptop = models.ForeignKey(Laptop, on_delete = models.CASCADE)
#     program = models.ForeignKey(Program, on_delete = models.CASCADE)
#     graphic = models.ForeignKey(Graphic, on_delete = models.CASCADE)