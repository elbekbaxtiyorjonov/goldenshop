from django.shortcuts import render
from .models import Sipochka


def sipochka(request):
    sipochka = Sipochka.objects.all().order_by('-id')
    context = {
        'sipochka': sipochka
    }
    return render(request=request, template_name='sipochka.html', context=context)