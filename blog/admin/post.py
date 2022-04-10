from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Meta fields', {
            'fields': (
                'title', 'slug', 'category', 'status',
                'author', 'created_on', 'rating', 'keywords',
            )
        }),
        ('Content fields', {
            'fields': (
                'preview_image', 'emoji_description',
                'short_description', 'content'),
        }),
    )