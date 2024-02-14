from django.shortcuts import render
from .models import Uzuklar


def index(request):
    uzuklar = Uzuklar.objects.all().order_by('-id')
    context = {
        'uzuklar': uzuklar
    }
    return render(request=request, template_name='index.html', context=context)
