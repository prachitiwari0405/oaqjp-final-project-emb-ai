import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_joy(self):
        statement = "I am glad this happened"
        self.assertEqual(emotion_detector(statement), "joy")
    
    def test_anger(self):
        statement = "I am really mad about this"
        self.assertEqual(emotion_detector(statement), "anger")
    
    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        self.assertEqual(emotion_detector(statement), "disgust")
    
    def test_sadness(self):
        statement = "I am so sad about this"
        self.assertEqual(emotion_detector(statement), "sadness")
    
    def test_fear(self):
        statement = "I am really afraid that this will happen"
        self.assertEqual(emotion_detector(statement), "fear")

if __name__ == "__main__":
    unittest.main()
statement = "I am really mad about this"
print(emotion_detector(statement))

