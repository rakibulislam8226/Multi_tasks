
from django.contrib import admin
from django.urls import path
from youtube import views as bviews
from translator import views as tviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('youtube/', bviews.youtube, name='youtube'),
    path('translate/', tviews.translate_app, name='trans')
]
