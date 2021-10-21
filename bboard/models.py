from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Stuff')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
