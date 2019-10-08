from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^form/?$', views.form,name="form"),
]