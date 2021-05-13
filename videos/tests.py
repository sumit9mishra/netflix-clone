from django.test import TestCase

from .models import Video

class VideoModelTestCase(TestCase):
    def setUp(self) :
        Video.objects.create(title ="first title")
    def test_value_title(self):
        title = "first title"
        qs = Video.objects.filter(title = title)
        self.assertTrue(qs.exists())

