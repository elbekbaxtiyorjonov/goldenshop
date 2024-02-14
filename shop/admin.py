from django.contrib import admin
from .models import Uzuklar


@admin.register(Uzuklar)
class UzuklarAdmin(admin.ModelAdmin):
    class Meta:
        model = Uzuklar
