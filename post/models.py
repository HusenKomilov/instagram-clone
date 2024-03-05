from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from utils.models import BaseModel
from users.models import User, BaseUser


class Location(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Post(BaseModel):
    description = models.TextField(blank=True, null=True)
    accessibility = models.TextField(blank=True, null=True)

    like = models.IntegerField(default=0, editable=False)
    comment = models.IntegerField(default=0, editable=False)
    watched = models.IntegerField(default=0, editable=False)

    user = models.ManyToManyField(User, related_name="post_users")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True, related_name="location")

    is_like_count = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=False)


class PostFiles(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_file")
    files = models.FileField(upload_to="post/",
                             validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "avi", "mp4"])])


class Story(BaseModel):
    file = models.FileField(upload_to="story/",
                            validators=[
                                FileExtensionValidator(allowed_extensions=['mp4', 'jpg', 'png', 'jpeg', 'mp3'])])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="save_post")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="story_user")


class Saved(BaseModel):
    post = models.ForeignKey(PostFiles, on_delete=models.CASCADE, related_name="saved_post")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="saved_user")


class Archive(BaseModel):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="archive_story")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="archive_user")


class Chat(BaseUser):
    chat = models.TextField()
    file = models.FileField(upload_to='chat/',
                            validators=[
                                FileExtensionValidator(allowed_extensions=['mp3', 'mp4', 'jpg', 'jpeg', 'png'])])
    
