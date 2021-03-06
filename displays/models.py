from django.db import models


# Create your models here.
class DisplayImage(models.Model):
    slider_image = models.ImageField(upload_to='slider/images/')
    header_text = models.CharField(max_length=120, null=True, blank=True)
    text = models.CharField(max_length=120, null=True, blank=True)
    about_display = models.BooleanField(default=False)
    active_slides = models.BooleanField(default=True)
    home_background_display = models.BooleanField(default=False)

    def __str__(self):
        return str(self.active_slides)


class Logo(models.Model):
    logo_image = models.ImageField(upload_to="logo/images/")
    title = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.active)



