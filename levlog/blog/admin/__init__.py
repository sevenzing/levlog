from blog.models import Post
from django.contrib import admin


from .post import PostAdmin


admin.site.register(Post, PostAdmin)
