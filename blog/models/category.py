
from django.db import models
from django.utils.translation import gettext as _



class Category(models.Model):
    name = models.CharField(max_length=100)
    image_svg = models.FileField(
        upload_to='category_images/', 
        verbose_name=_('image'),
    )

    def __str__(self) -> str:
        return self.name.title()

    class Meta:
        verbose_name_plural = 'categories'