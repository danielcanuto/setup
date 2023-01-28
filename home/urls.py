from django.urls import path
from home.views import IndexView
from home.views import SobreView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
]