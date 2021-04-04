from django.contrib import admin
from django.urls import path
from .views import Index, Create, Complete, Archive, Delete, Update, Recover

urlpatterns = [
    path('tasks', Index.as_view(), name="tasks.index"),
    path('tasks/<int:pk>/complete', Complete.as_view(), name="tasks.complete"),
    path('tasks/<int:pk>/archive', Archive.as_view(), name="tasks.archive"),
    path('tasks/<int:pk>/recover', Recover.as_view(), name="tasks.recover"),
    path('tasks/create', Create.as_view(), name="tasks.create"),
    path('tasks/<int:pk>/edit', Update.as_view(), name="tasks.edit"),
    path('tasks/<int:pk>/delete', Delete.as_view(), name="tasks.delete"),
]