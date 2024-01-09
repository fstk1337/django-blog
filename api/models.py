from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='', default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created']
