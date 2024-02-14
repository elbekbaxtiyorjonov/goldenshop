from django.shortcuts import render
from .models import Hodimlar


def hodimlar(request):
    hodimlar = Hodimlar.objects.all()
    context = {
        'hodimlar': hodimlar
    }
    return render(request=request, template_name='hodimlar.html', context=context)