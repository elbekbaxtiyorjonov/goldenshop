from django.db import models


class Uzuklar(models.Model):
    image = models.ImageField(blank=True, null=True)
    size = models.CharField(max_length=255)
    gramm = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)
    murojat = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def imageURL(self):
        return self.image.url

    def __str__(self):
        return f"{self.image} -- {self.narxi}"
