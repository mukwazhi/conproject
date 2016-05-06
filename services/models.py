from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = RichTextField(max_length=1500)
    slug = models.SlugField(unique=True)
    active = models.BooleanField()
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ServicesImage(models.Model):
    title = models.ForeignKey(Service)
    image = models.ImageField(upload_to='services/images/')
    active = models.BooleanField(default=True)

