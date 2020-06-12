from django.urls import include, path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('transact/', views.trans_email),
    path('snippets/<int:pk>', views.tran_email)
]

urlpatterns = format_suffix_patterns(urlpatterns)