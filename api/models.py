from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    
    class Meta:
        verbose_name_plural = 'categories'

