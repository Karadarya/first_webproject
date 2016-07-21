from django.contrib import admin
from .models import Post, Tag, Score


class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','public_post', 'published_date')
    list_editable = ('public_post',)
    list_filter = ('author', 'public_post')
    search_fields = ['title', 'text']
    readonly_fields = ('published_date',)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Score)
# Register your models here.
