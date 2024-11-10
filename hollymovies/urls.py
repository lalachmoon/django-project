from django.contrib import admin
from django.urls import path

from viewer.views import home, film, genre


urlpatterns = [
    path('admin/', admin.site.urls),

    # Parametrii cu regular expressions
    # path('hello/<s>/<other_s>', hello)

    # Parametrii cu URL Encoding
    path('', home, name='home'),

    path('film/<slug:my_slug>/', film, name='film'),

    # Genre path
    path('genre/<slug:my_slug>/', genre, name='genre'),


]
