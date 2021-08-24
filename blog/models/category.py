from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext as _
from tinymce.models import HTMLField
from stdimage import StdImageField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = StdImageField(
        upload_to='category_images/', 
        null=True,
        variations={
            'small' : {'width': 64, 'height': 64}
        },
        verbose_name=_('image'),
    )

    def __str__(self) -> str:
        return self.name.title()

    class Meta:
        verbose_name_plural = 'categories'