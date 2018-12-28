from django import template
from photoalbum.models import Comment, Likes, Photo, Follow

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
def count_followers(user):
    followers = Follow.objects.filter(user_followed_id=user.id, follow=True)
    return len(followers)


@register.filter()
def likes_id(photo):
    likes = Likes.objects.filter(photo_id=photo.id, like=True)
    list_id = likes.values_list('user_id', flat=True)
    return list_id


@register.filter()
def follow_id(user):
    follows = Follow.objects.filter(user_followed_id=user.id, follow=True)
    list_id = follows.values_list('user_follower_id', flat=True)
    return list_id
