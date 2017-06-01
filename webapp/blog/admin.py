from django.contrib import admin

from .models import Post, Tag, Comment, ApplicationMenuItem


class ApplicationMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(ApplicationMenuItem, ApplicationMenuItemAdmin)
