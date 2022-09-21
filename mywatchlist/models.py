from django.db import models

# Create your models here.
class ItemMyWatchList(models.Model):
    item_watched = models.BooleanField()
    item_title = models.CharField(max_length=255)
    item_rating = models.IntegerField()
    item_release_date = models.DateField()
    item_review = models.TextField()