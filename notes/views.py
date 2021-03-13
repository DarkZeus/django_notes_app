from django.shortcuts import render
from .models import Note
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Index(LoginRequiredMixin, ListView):
    template_name = 'notes/index.html'
    context_object_name = 'notes'
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')


class Show(UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'notes/show.html'
    context_object_name = 'note'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False


class Create(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/create.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'notes/update.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False


class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'notes/delete.html'
    context_object_name = 'note'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False


def about(request):
    return render(request, 'notes/about.html')
