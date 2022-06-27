from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

def index(request):
    return render(request, 'textscoring/home.html')


class AddRecord(CreateView):
    form_class = RecordForm
    template_name = 'textscoring/add_results.html'

    def form_valid(self, form):
        super(AddRecord, self).form_valid(form)
        record = UserRecord.objects.last()
        rec = {
            "record": record
        }
        return render(self.request, 'textscoring/home.html', {'record': record})