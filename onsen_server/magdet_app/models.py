from django.db import models


class availability(models.Model):
    room = models.PositiveSmallIntegerField()
    lock = models.BooleanField()

    def __str__(self):
        obj_room = f"room{str(self.room)}"
        return obj_room
