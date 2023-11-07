from django.shortcuts import render, get_object_or_404
from contacts.models import Contact
from feedback.models import StatusFeedback
from feedback.forms import FeedbackForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def contact_list(request):
    status = get_object_or_404(StatusFeedback,
                               id=1)
    form = FeedbackForm(request.POST or None,
                        initial={'status': status,
                                  })  # параметры по умолчанию

    if request.method == 'POST':
        if form.is_valid():
            form.save()  # сохрание данных в БД
            url = reverse('contacts',  # адрес на кот. пойдет redirect
                          kwargs={})  # параметры для адреса
            return HttpResponseRedirect(f'{url}?sent=1')  # sent - GET параметр

    contacts = Contact.objects.all()
    return render(request,
                  'contact_list.html',
                  {'contacts': contacts,
                   'form': form,
                   'sent': request.GET.get('sent')
                   }
                  )
