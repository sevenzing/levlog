from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from tinymce.models import HTMLField


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, 'Draft')
        PUBLISHED = (1, 'Published')
        HIDDEN = (2, 'Hidden')
        DELETED = (3, 'Deleted')


    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
    )
    
    updated_on = models.DateTimeField(auto_now=True, verbose_name=_('last update'))
    content = HTMLField(verbose_name=_('content'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('creation time'))
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name=_('status'))
    views = models.IntegerField(default=0, verbose_name=_('views'))

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}({self.views})"
