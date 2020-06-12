from django.urls import include, path
from rest_framework.routers import DefaultRouter

from django.conf.urls.static import static
from django.conf import settings


from . import views

router = DefaultRouter()
router.register('tracks', views.TrackViewSet, basename='track')
router.register('search', views.SearchViewSet, basename='search')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))
]