from django.shortcuts import render
from .models import Braslet


def braslet(request):
    braslet = Braslet.objects.all().order_by('-id')
    context = {
        'braslet': braslet
    }
    return render(request=request, template_name='braslet.html', context=context)