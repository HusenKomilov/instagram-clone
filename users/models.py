from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utils.choices import Gender
from utils.models import BaseModel


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None
    last_name = None

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    website = models.URLField()
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=128, choices=Gender.choices)

    avatar = models.ImageField(upload_to="profile/avatar/", blank=True, null=True)
    image = models.ImageField(upload_to="profile/image/", blank=True, null=True)

    is_suggestions = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    is_quiet_mode = models.BooleanField(default=False)
    is_save = models.BooleanField(default=True)
    is_check = models.BooleanField(default=False)


class Followers(BaseModel):
    from_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    to_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_confirm = models.BooleanField(default=True)


class Following(BaseModel):
    from_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    to_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
