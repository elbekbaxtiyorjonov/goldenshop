from django.contrib import admin
from .models import Ziraklar


@admin.register(Ziraklar)
class UzuklarAdmin(admin.ModelAdmin):
    class Meta:
        model = Ziraklar