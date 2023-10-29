from django.db import models


class Note(models.Model):
    summary = models.CharField(max_length=250, verbose_name='Опис проблеми')
    label = models.CharField(max_length=50, verbose_name='Ярлик')
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Вирішення проблеми')

    class Meta:
        verbose_name = 'Нотатка'
        verbose_name_plural = 'Нотатки'
        ordering = ['-date']
