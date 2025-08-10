from django.contrib import admin

from .models import Product, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'active', 'points']

    # remove empty fields 
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]
  #  fields = ['title']

    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'date_created', 'active', ]
  #  search_fields = ['author', 'active', ]

