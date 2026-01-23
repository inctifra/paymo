from django.urls import path

from . import views


app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.index, name="about"),
    path("transactions/", views.transactions_view, name="transactions"),
]
