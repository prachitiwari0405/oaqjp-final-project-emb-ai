import requests

# URL and Headers for Watson NLP Library
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    input_json = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(URL, headers=HEADERS, json=input_json)
        response.raise_for_status()
        
        # Print the full response for debugging
        print("Full Response:", response.json())
        
        # Extract emotion data from the response
        emotion_data = response.json().get('emotionPredictions', [])
        
        if emotion_data:
            # Access the first emotion prediction
            emotions = emotion_data[0].get('emotion', {})
            return emotions
        else:
            return "No emotion data available."
        
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
