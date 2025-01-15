import requests

# Watson NLP Emotion Detection API URL and Headers
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

class EmotionPredict:
    """
    A class to interact with the Watson Emotion Prediction API and predict emotions from text input.

    Methods:
        get_emotion_response(statement): Sends a request to the Watson Emotion Prediction API and returns the response.
        predict_emotion(statement): Analyzes the emotion of a given text statement.
    """
    def __init__(self):
        """Initializes the EmotionPredict class."""
        pass

    def get_emotion_response(self, statement):
        """
        Sends a request to the Watson API and returns the response.

        Args:
            statement (str): The text for which emotion analysis is requested.

        Returns:
            dict: A dictionary containing the status code and predicted emotions.
        """
        if not statement:
            print("Error: Statement is empty!")
            # Return a response for blank input
            return {"status_code": 400, "emotionPredictions": [{"emotion": None}]}

        data = {
            "raw_document": {
                "text": statement  # Pass the text to analyze under "text"
            }
        }

        try:
            response = requests.post(URL, headers=HEADERS, json=data)
            if response.status_code == 200:
                return response.json()  # Return the JSON response
            else:
                print(f"Error: Received status code {response.status_code}")
                return {"status_code": response.status_code, "emotionPredictions": [{"emotion": None}]}
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return {"status_code": 500, "emotionPredictions": [{"emotion": None}]}

    def predict_emotion(self, statement):
        """
        Predicts emotion from a given statement.

        Args:
            statement (str): The text to predict emotion for.

        Returns:
            dict: A dictionary containing the predicted emotion or error message.
        """
        if not statement.strip():  # Check for blank entries
            return {"error": "Input text cannot be empty!"}

        response = self.get_emotion_response(statement)

        if response.get("status_code") == 400:  # Handle invalid input
            return {"error": "Invalid text! Please try again!"}

        try:
            emotion_scores = response['emotionPredictions'][0]['emotion']
        except (KeyError, IndexError) as e:
            print(f"Error extracting emotions: {e}")
            return {"error": "Invalid text! Please try again!"}

        if not emotion_scores:
            return {"error": "Invalid text! Please try again!"}

        # Get the dominant emotion with the highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        return {"predicted_emotion": dominant_emotion}


class EmotionDetector:
    """
    A class to determine emotions from text input using the EmotionPredict class.

    Methods:
        predict_emotion(text): Uses EmotionPredict to determine the emotion from the provided text.
    """
    def __init__(self):
        """Initializes the EmotionDetector class and its EmotionPredict instance."""
        self.emotion_predictor = EmotionPredict()

    def predict_emotion(self, text):
        """
        Uses EmotionPredict to determine the emotion of the input text.

        Args:
            text (str): The text to predict emotion for.

        Returns:
            dict: A dictionary containing the predicted emotion or an error message.
        """
        if not text:
            return {"error": "Input text cannot be empty!"}

        result = self.emotion_predictor.predict_emotion(text)

        if 'error' in result:
            return result

        return {"predicted_emotion": result["predicted_emotion"]}

               
        
