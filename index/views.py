from django.shortcuts import render


def index(request):
    return render(request,
                  'hotel/main_page.html',
                  {'sent': request.GET.get('sent'), # из room_detail
                   }
                  )
