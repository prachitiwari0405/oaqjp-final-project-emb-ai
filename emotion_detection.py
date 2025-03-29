from transformers import pipeline

class EmotionDetector:
    def __init__(self):
        # Load a pre-trained emotion detection model from the transformers library
        self.model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    def predict_emotion(self, text):
        try:
            # Use the model to predict the emotion of the input text
            result = self.model(text)
            # Extract the predicted emotion with the highest score
            predicted_emotion = result[0]['label']
            return {"predicted_emotion": predicted_emotion}
        except Exception as e:
            return {"error": str(e)}
