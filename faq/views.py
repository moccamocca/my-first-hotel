from django.shortcuts import render
from faq.models import Faq


def faq(request):
    faq_all = Faq.objects.all();
    return render(request,
                  'faq.html',
                  {'faq_all': faq_all, })
