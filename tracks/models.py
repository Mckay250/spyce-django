import uuid

from django.db import models
from s3direct.fields import S3DirectField


# Create your models here.
def artwork_path(instance, filename):
    return '/'.join(['artworks', filename])

def mp3_path(instance, filename):
    return '/'.join(['audio', 'mp3', filename])

def wav_path(instance, filename):
    return '/'.join(['audio', 'wav', filename])

def sample_audio_path(instance, filename):
    return '/'.join(['audio', 'sample_audio', filename])

class Track(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    bpm = models.IntegerField(null=False)
    mp3_price = models.FloatField(null=False)
    price = models.FloatField()
    wav_price = models.FloatField(null=False)
    key = models.CharField(max_length=7)
    tags = models.CharField(null=True, max_length=256)
    in_cart = models.BooleanField(default=False)
    track_status = models.CharField(max_length=20, default='not-clicked')
    selected_type = models.CharField(max_length=7, default='mp3')
    sample_audio = models.FileField(blank=False, upload_to='media/sample_audio')
    mp3 = models.FileField(blank=False, upload_to='media/mp3')
    wav = models.FileField(blank=False, upload_to='media/wav')
    artwork = models.FileField(blank=False, upload_to='media/artowrk')
    # artwork = S3DirectField(dest='primary_destination', blank=True, null=True)
    # sample_audio = S3DirectField(dest='primary_destination', blank=True)
    # mp3 = S3DirectField(dest='primary_destination', blank=True)
    # wav = S3DirectField(dest='primary_destination', blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title