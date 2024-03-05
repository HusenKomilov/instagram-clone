from django.db import models


class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    CUSTOM = "CUSTOM", "Custom"
    NOT_SAY = "PREFER NOT TO SAY", "Prefer not to say"
