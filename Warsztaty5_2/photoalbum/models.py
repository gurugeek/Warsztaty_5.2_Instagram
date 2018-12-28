from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    path = models.ImageField(upload_to='photos/')
    content = models.CharField(max_length=256)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.content[0:50]}'


class Comment(models.Model):
    content = models.CharField(max_length=60)
    creation_date = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.photo} {self.content[0:50]}"


class Likes(models.Model):
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.photo}: {self.like}"


class Message(models.Model):
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_to")
    sent_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_from")
    read = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"To: {self.sent_to}, From: {self.sent_from}, Text: {self.content[0:30]}"


class Follow(models.Model):
    follow = models.BooleanField()
    user_follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    user_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")

    def __str__(self):
        return f"{self.follower} - {self.followed}: {self.follow}"
