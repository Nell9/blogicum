from django.contrib import admin
from .models import Location, Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'is_published'
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
