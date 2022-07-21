from django.db import models
from model_utils import FieldTracker


class availability(models.Model):
    room = models.PositiveSmallIntegerField()
    lock = models.BooleanField()

    tracker = FieldTracker()

    def __str__(self):
        obj_room = f"room{str(self.room)}"
        return obj_room
