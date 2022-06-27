from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import UserRecord
from django.contrib.auth.models import User
from .services.pol2_idf_tf import *
import pickle
import os


class RecordForm(ModelForm):


    class Meta:
        model = UserRecord
        fields = ('input_text1', 'input_text2',)
        widgets = {
            'input_text1': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
            'input_text2': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }

    def save(self, commit=True):
        record = super(RecordForm, self).save(commit)
        text1 = self.cleaned_data['input_text1']
        text2 = self.cleaned_data['input_text2']

        line1 = line_norm(text_line(text1))
        line2 = line_norm(text_line(text2))

        count1 = ' '.join(map(str, tf_count(line1)))
        count2 = ' '.join(map(str, tf_count(line2)))

        norm_both_lists = [line1, line2]

        record.text1_count_out = count1
        record.text2_count_out = count2
        record.both_texts_IDF_TF_out = ' '.join(map(str, compute_tfidf(norm_both_lists)))


        record.save()
        return record