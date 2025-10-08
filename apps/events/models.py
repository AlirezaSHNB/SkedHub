from django.db import models
from django.conf import settings

class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="organized_events"
    )

    def __str__(self):
        return self.title


class EventSessionManager(models.Manager):
    def upcoming(self):
        from django.utils import timezone
        return self.filter(start__gte=timezone.now())


class EventSession(models.Model):
    event = models.ForeignKey(Event, related_name='sessions', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    capacity = models.PositiveIntegerField(default=0)
    venue = models.ForeignKey(Venue, null=True, on_delete=models.SET_NULL)

    objects = EventSessionManager()

    class Meta:
        ordering = ['start']

    def __str__(self):
        return f"{self.event.title} @ {self.start.strftime('%Y-%m-%d %H:%M')}"
