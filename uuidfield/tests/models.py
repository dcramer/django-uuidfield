import uuid
from django.db import models
from uuidfield import UUIDField


class AutoUUIDField(models.Model):
    uuid = UUIDField(auto=True)


class HyphenatedUUIDField(models.Model):
    uuid = UUIDField(auto=True, hyphenate=True)
    name = models.CharField(max_length=16)


class ManualUUIDField(models.Model):
    uuid = UUIDField(auto=False)


class NamespaceUUIDField(models.Model):
    uuid = UUIDField(auto=True, namespace=uuid.NAMESPACE_URL, version=5)


class BrokenNamespaceUUIDField(models.Model):
    uuid = UUIDField(auto=True, namespace='lala', version=5)
