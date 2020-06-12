from django.contrib import admin

from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'items', 'types', 'total')


# Register your models here.
admin.site.register(Transaction, TransactionAdmin)