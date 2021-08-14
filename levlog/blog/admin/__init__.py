from blog import models
from django.contrib import admin


from .post import PostAdmin
from .user import UserAdmin


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.User, UserAdmin)
