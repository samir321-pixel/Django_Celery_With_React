from django.urls import path
from .views import SendMail, IndexView


urlpatterns = [
    path('sendmail/', SendMail.as_view()),
    path('', IndexView.as_view(), name='index')
]
