
from django.contrib import admin
from django.urls import path
from youtube import views as bviews
from translator import views as tviews
from multi_mail import views as multi_mail_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('youtube/', bviews.youtube, name='youtube'),
    path('translate/', tviews.translate_app, name='trans'),
    path('multi_mail/', multi_mail_views.usersList.as_view(), name='users'),
]
