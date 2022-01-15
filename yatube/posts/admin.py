from django.contrib import admin

from .models import Post, Group


EMPTY_VALUE = '-пусто-'

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text', 'pub_date', 'group',)
    list_editable = ('group',)
    list_filter = ('pub_date',)
    search_fields = ('text',)
    empty_value_display = EMPTY_VALUE


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
