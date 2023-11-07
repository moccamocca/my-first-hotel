"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rooms.views import rooms_list, room_detail
from index.views import index
from contacts.views import contact_list
from booking.views import booking_filter
from faq.views import faq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', rooms_list, name='rooms'),
    path('', index, name='home'),
    path('contacts/', contact_list, name='contacts'),
    path('booking/', booking_filter, name='booking_filter'),
    path('room/<int:room_id>_<str:date_in>_<str:date_out>_<int:count_adult>_<int:count_night>/', room_detail, name='room_detail'),
    path('faq/', faq, name='faq'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# для отладки
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

# --------------
admin.site.site_header = 'Администрирование сайта ОТЕЛЬ .... urls.py'                    # default: "Django Administration"
# admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'эта переменная в urls.py'   # default: "Django site admin"
