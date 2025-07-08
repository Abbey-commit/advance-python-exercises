from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'riddles'

urlpatterns = [
    url(r'^riddles/', include('riddles.urls')),
    url(r'^admin/', admin.site.urls),
]