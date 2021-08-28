from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext as _
from tinymce.models import HTMLField
from stdimage import StdImageField


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-rating', '-created_on')


class AvaliablePostManager(PostManager):
    def get_queryset(self):
        return super().get_queryset().filter(
            status=Post.Status.PUBLISHED
        )


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
    
    preview_image = StdImageField(
        upload_to='uploads/%Y/%m/%d/',
        null=True,
        variations={
            'cropped': {'width': 1000, 'height': 400, 'crop': True},
            'small': {'width': 400, 'height': 400},
            'box' : {'width': 400, 'height': 400, 'crop': True}
        },
        verbose_name=_('preview'),
    )
    updated_on = models.DateTimeField(auto_now=True, verbose_name=_('last update'))
    
    short_description = HTMLField(verbose_name=_('short'), null=True)
    emoji_description = models.CharField(max_length=10, verbose_name=_('emoji'), null=True)
    content = HTMLField(verbose_name=_('content'))

    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('creation time'))
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name=_('status'))
    
    rating = models.IntegerField(default=1, verbose_name=_('rating'))
    category = models.ForeignKey(
        to='blog.category', 
        on_delete=models.CASCADE,
        verbose_name=_('category'),
        null=True,
        blank=True,
    )

    objects = PostManager()
    avaliable_objects = AvaliablePostManager()

    @property
    def views(self):
        """
        Amount of views is amount if unique ips that accessed that post
        """
        return PostView.objects.filter(post=self).count()

    def get_absolute_url(self):
        return reverse('blog.post_view', args=(self.slug,))

    def __str__(self):
        return f'{self.title}({self.views})'


class PostView(models.Model):
    ip = models.GenericIPAddressField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('post view')
        verbose_name_plural = _('post views')

    def __str__(self):
        return f'{self.ip} in {self.post}'
