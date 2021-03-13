from django.contrib import admin
from django.urls import path
from .views import Index, Show, Create, Update, Delete
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('notes.index', permanent=False)),
    path('notes', Index.as_view(), name="notes.index"),
    path('notes/<int:pk>/', Show.as_view(), name="notes.show"),
    path('notes/create', Create.as_view(), name="notes.create"),
    path('notes/<int:pk>/edit', Update.as_view(), name="notes.edit"),
    path('notes/<int:pk>/delete', Delete.as_view(), name="notes.delete"),


    path('about', views.about, name="notes.about"),
]