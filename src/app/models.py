from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, verbose_name='Contenue')
    last_update = models.DateField(auto_now=True, verbose_name='Dernière modification')
    published = models.BooleanField(default=False, verbose_name='Publié', blank=True)
    slug = models.SlugField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name_plural = 'Articles'
        unique_together = ['title', ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title