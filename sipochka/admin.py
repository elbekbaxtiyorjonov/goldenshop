from django.contrib import admin
from .models import Sipochka


@admin.register(Sipochka)
class UzuklarAdmin(admin.ModelAdmin):
    class Meta:
        model = Sipochka