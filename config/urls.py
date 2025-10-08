from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.events.viewsets import VenueViewSet, EventViewSet, EventSessionViewSet
from apps.bookings.viewsets import BookingViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet)
router.register(r'events', EventViewSet)
router.register(r'sessions', EventSessionViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
