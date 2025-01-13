import requests

# URL and Headers for Watson NLP Emotion Detection API
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def get_emotion_response(statement):
    # Sending the statement to the Watson NLP API
    data = {"document": statement}  # Adjusted the key here to 'document'
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            return response.json()  # Return the response in JSON format
        else:
            print(f"Error: Received status code {response.status_code}")
            print(response.text)  # Print the error response
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def emotion_detector(statement):
    # Get emotion predictions from the API
    response = get_emotion_response(statement)
    
    # If response is None, return None (handle error)
    if not response:
        return None
    
    print("API Response:", response)  # Print the full API response for debugging
    
    # Assuming the response contains a dictionary with emotion predictions (adjust this as necessary)
    try:
        emotion_scores = response['emotionPredictions'][0]['emotion']
    except (KeyError, IndexError) as e:
        print(f"Error extracting emotions from response: {e}")
        return None

    # Get the dominant emotion with the highest score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return dominant_emotion

# Example test
statement = "I am really mad about this"
print("Detected Emotion:", emotion_detector(statement))
