from django.test import TestCase


class AppTest(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)