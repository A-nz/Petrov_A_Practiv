from django.db import models


class UserRecord(models.Model):
    input_text1 = models.TextField(max_length=10000)
    input_text2 = models.TextField(max_length=10000)

    text1_count_out = models.TextField(max_length=10000)
    text2_count_out = models.TextField(max_length=10000)
    both_texts_IDF_TF_out = models.TextField(max_length=10000)


    def get_absolute_url(self):
        return '/'
