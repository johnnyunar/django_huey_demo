from django.db import models


class Activity(models.Model):
    class Meta:
        verbose_name_plural = "Activities"

    name = models.CharField(max_length=256)
    type = models.CharField(max_length=128)
    participants = models.IntegerField()
    price = models.FloatField()
    link = models.CharField(max_length=256, blank=True)
    key = models.CharField(max_length=128, blank=True)
    accessibility = models.FloatField()

    def __str__(self):
        return self.name
