from django.db import models

class RatingsChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    synopsis = models.TextField(null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingsChoices.choices,
        default=RatingsChoices.G
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )