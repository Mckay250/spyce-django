from django.contrib import admin

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bpm', 'key', 'tags', 'mp3_price', 'wav_price' )


# Register your models here.
admin.site.register(Track, TrackAdmin)