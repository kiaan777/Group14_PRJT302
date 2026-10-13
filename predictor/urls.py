from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("clear-history/", views.clear_history, name="clear_history"),
]
