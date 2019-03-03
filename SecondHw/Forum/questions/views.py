from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from questions.models import Question


class QuestionCreate(CreateView):
    model = Question
    template_name = 'questionSave.html'
    fields = ['question']


class QuestionUpdate(UpdateView):
    model = Question
    template_name = 'questionUpdate.html'
    fields = ['question']


class QuestionDelete(DeleteView):
    model = Question
    template_name = 'questionDelete.html'
    fields = ['question']


class QuestionView(ListView):
    model = Question
    template_name = 'questionView.html'
    fields = ['question']
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['createForm'] = QuestionCreate.get_form_class(QuestionCreate())
        return context
