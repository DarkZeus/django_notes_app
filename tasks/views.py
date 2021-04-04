from .models import Task
from .forms import CreateTaskForm, UpdateTaskForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Index(ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    paginate_by = 25

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')


class Complete(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['is_done']

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.is_done = True
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False


class Archive(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['is_archived']

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.is_archived = True
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False


class Create(LoginRequiredMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'tasks/update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False


class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/tasks'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

        return False
