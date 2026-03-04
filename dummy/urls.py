from django.urls import path
from .views import to
urlpatterns = [
    path('to/',to.as_view(),name='to')
]