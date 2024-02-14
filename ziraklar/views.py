from django.shortcuts import render
from .models import Ziraklar


def ziraklar(request):
    ziraklar = Ziraklar.objects.all().order_by('-id')
    context = {
        'ziraklar': ziraklar
    }
    return render(request=request, template_name='uzuklar.html', context=context)