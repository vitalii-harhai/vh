from django.db import models


class CatalogName(models.Model):
    priority = models.IntegerField(verbose_name='Пріорітет', default=0)
    name = models.CharField(max_length=250, verbose_name='Назва')
    user = models.CharField(max_length=250, verbose_name='Користувач')

    def __str__(self):
        return self.name


class LinkList(models.Model):
    priority = models.IntegerField(verbose_name='Пріорітет')
    name = models.CharField(max_length=250, verbose_name='Назва')
    link = models.CharField(max_length=250, verbose_name='Посилання')
    catalog = models.ForeignKey(CatalogName, on_delete=models.CASCADE, verbose_name='Каталог')
    user = models.CharField(max_length=250, verbose_name='Користувач')

    def __str__(self):
        return f'{self.name} ({self.catalog})'
