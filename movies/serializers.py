from email.policy import default
from rest_framework import serializers

from .models import Movie, RatingsChoices

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, allow_null=True)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.EmailField(read_only=True, source="user.email")

    rating = serializers.ChoiceField(
        choices=RatingsChoices.choices,
        default=RatingsChoices.G
    )

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)