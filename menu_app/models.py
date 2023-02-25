from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name menu')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name='Item title')
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'