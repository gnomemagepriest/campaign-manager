from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="campaign")

    def __str__(self) -> str:
        return self.title
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="item")

    def __str__(self) -> str:
        return self.name
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="character")

    def __str__(self) -> str:
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="location")

    def __str__(self) -> str:
        return self.name
    
class Quest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="quest")

    def __str__(self) -> str:
        return self.name