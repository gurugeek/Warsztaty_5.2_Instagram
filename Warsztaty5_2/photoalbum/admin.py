from django.contrib import admin

from .models import *


def short_content(text):
    return str(text.content)[0:50]


def block(model_admin, request, query_set):
    query_set.update(blocked=True)


@admin.register(Photo)
class TweetAdmin(admin.ModelAdmin):
    list_display = ["id", short_content, "user", "creation_date", "blocked"]
    list_filter = ["user", "creation_date", "blocked"]
    actions = [block, ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "sent_date", "sent_from", "sent_to", short_content, "read", "blocked"]
    list_filter = ["sent_to", "sent_from", "sent_date", "read", "blocked"]
    actions = [block, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "creation_date", "photo", "user", short_content, "blocked"]
    list_filter = ["user", "creation_date", "blocked"]
    actions = [block, ]


@admin.register(Likes)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "like", "user", "photo", "blocked"]
    list_filter = ["user", "blocked"]
    actions = [block, ]
