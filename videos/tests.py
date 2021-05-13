from django.test import TestCase

from .models import Video

class VideoModelTestCase(TestCase):
    def setUp(self) :
        Video.objects.create(title ="first title")
    def test_value_title(self):
        title = "first title"
        qs = Video.objects.filter(title = title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(),1)

