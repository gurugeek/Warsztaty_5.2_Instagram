from django import template
from photoalbum.models import Comment, Likes, Photo

register = template.Library()


@register.filter()
def count_comments(photo):
    comments = Comment.objects.filter(photo_id=photo.id)
    return len(comments)


@register.filter()
def count_likes(photo):
    likes = Likes.objects.filter(photo_id=photo.id, like=True)
    return len(likes)


@register.filter()
def likes_id(photo):
    likes = Likes.objects.filter(photo_id=photo.id, like=True)
    list_id = likes.values_list('user_id', flat=True)
    return list_id