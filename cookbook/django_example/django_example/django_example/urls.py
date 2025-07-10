from django.urls import include, path
from django.contrib import admin
from riddles import views  # Import riddles views for the root URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('riddles/', include('riddles.urls')),
    path('', views.index, name='home'),  # Added root URL to riddles index
]