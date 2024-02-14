from django.contrib import admin
from .models import Braslet


@admin.register(Braslet)
class UzuklarAdmin(admin.ModelAdmin):
    class Meta:
        model = Braslet