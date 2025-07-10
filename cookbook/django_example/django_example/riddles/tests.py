from django.test import TestCase
from .models import Riddle

# Create your tests here.

class RiddleModelTest(TestCase):
    def setUp(self):
        Riddle.objects.create(question="What has keys but can't open locks?", answer="A piano")

    def test_riddle_str(self):
        riddle = Riddle.objects.get(id=1)
        self.assertEqual(str(riddle), "What has keys but can't open locks?")