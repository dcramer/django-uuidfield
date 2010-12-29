from django.db import models

from uuidfield import UUIDField

class UUIDFieldTestModel(models.Model):
    uuid = UUIDField(auto=True)
