from django.db import models


class Portfolio(models.Model):
    project_title = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    project_date = models.DateField()
    project_image = models.ImageField(upload_to='portfolio/images/')
    slug = models.SlugField(unique=True)
    display = models.BooleanField(default=False)


