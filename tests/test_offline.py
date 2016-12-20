from unittest import TestCase
import pyrealsense as pyrs
from pyrealsense.utils import RealsenseError

class TestStart(TestCase):
    def test_is_started(self):
        try:
            pyrs.start()
        except RealsenseError as e:
            self.assertTrue(e.function == 'rs_create_context')

class TestDevice(TestCase):
    def test_is_not_created(self):
        try:
            pyrs.Device()
        except RealsenseError as e:
            self.assertTrue(e.function == 'rs_get_device')
