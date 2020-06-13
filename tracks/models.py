import uuid

from django.db import models


# Create your models here.

class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    bpm = models.IntegerField(null=False)
    mp3_price = models.FloatField(null=False)
    price = models.FloatField(null=False)
    wav_price = models.FloatField(null=False)
    key = models.CharField(max_length=7)
    tags = models.CharField(null=True, max_length=256)
    in_cart = models.BooleanField(default=False)
    track_status = models.CharField(max_length=15, default='not-clicked')
    selected_type = models.CharField(max_length=7, default='mp3')
    sample_audio = models.FileField(blank=False, upload_to='media/sample_audio')
    mp3 = models.FileField(blank=False, upload_to='media/mp3')
    wav = models.FileField(blank=False, upload_to='media/wav')
    artwork = models.FileField(blank=False, upload_to='media/artwork')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title