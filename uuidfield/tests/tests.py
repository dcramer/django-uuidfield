from django.db import connection
from django.test import TestCase

from uuidfield.tests.models import UUIDFieldTestModel

import uuid

class UUIDFieldTestCase(TestCase):
    def test_auto_uuid4(self):
        inst = UUIDFieldTestModel.objects.create()
        self.assertTrue(inst.uuid)
        self.assertEquals(len(inst.uuid), 32)
        # self.assertTrue(isinstance(inst.uuid, uuid.UUID))
