import unittest
# Import the function from your package or application file
# Replace 'emotion_detection' with the actual name of your script file if it is different
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy_emotion(self):
        # Test for dominant emotion: joy
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result, "joy")

    def test_anger_emotion(self):
        # Test for dominant emotion: anger
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result, "anger")

    def test_disgust_emotion(self):
        # Test for dominant emotion: disgust
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result, "disgust")

    def test_sadness_emotion(self):
        # Test for dominant emotion: sadness
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result, "sadness")

    def test_fear_emotion(self):
        # Test for dominant emotion: fear
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result, "fear")

if __name__ == "__main__":
    unittest.main()