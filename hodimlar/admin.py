from django.contrib import admin
from .models import Hodimlar


@admin.register(Hodimlar)
class UzuklarAdmin(admin.ModelAdmin):
    class Meta:
        model = Hodimlar