from django.db import models
from django.contrib import admin

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    avatar = models.FileField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.username

class CommentSection(models.Model):
    # id = models.AutoField(primary_key=True)
    body = models.TextField(max_length=300, blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     comment = models.ForeignKey(CommentSection)


# class TvShow(models.Model):
#     title = models.CharField(max_length=30)

#     def __str__(self):
#         return self.title


# class Favorite(models.Model):
#     user = models.ForeignKey('User', related_name='favorites')
#     show = models.ForeignKey('TvShow', related_name='favorites')

#     def __str__(self):
#         return self.show

# class UserProfile(models.Model):
#     user = models.ForeignKey(User)
#     favorites = models.ForeignKey(Favorite)