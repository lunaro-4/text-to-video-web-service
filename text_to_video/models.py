from django.db import models



class RequestRecord(models.Model):
    date_field = models.DateField()
    text_field = models.TextField(blank=True, help_text='Enter text to animate')
    size_x_field = models.IntegerField(blank=True, help_text='Enter video width')
    size_y_field = models.IntegerField(blank=True, help_text='Enter video hight')
    fps_field = models.IntegerField(blank=True, help_text='Enter desired video fps')
    length_field = models.IntegerField(blank=True, help_text='Enter video length in seconds')
    
