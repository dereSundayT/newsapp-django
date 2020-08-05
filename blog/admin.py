from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "created_on", "publish"]

    class Meta:
        model = Comment


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
