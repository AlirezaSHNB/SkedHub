from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.events.viewsets import VenueViewSet, EventViewSet, EventSessionViewSet
from apps.bookings.viewsets import BookingViewSet
from apps.users.viewsets import UserViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet)
router.register(r'events', EventViewSet)
router.register(r'sessions', EventSessionViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
