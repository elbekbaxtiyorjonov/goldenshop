from django.db import models


class Hodimlar(models.Model):
    ism = models.CharField(max_length=255)
    familya = models.CharField(max_length=255)
    yosh = models.CharField(max_length=25)
    nomer = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    murojat = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ism} -- {self.familya}"
