import json

def emotion_detector(response_text):
    # Convert response text to dictionary
    response_dict = json.loads(response_text)
    
    # Extract required emotions
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_scores = {emotion: response_dict.get(emotion, 0) for emotion in emotions}
    
    # Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return formatted output
    return {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }

# Example response from IBM Watson
response_text = '{"anger": 0.1, "disgust": 0.05, "fear": 0.2, "joy": 0.7, "sadness": 0.15}'

# Test the function
formatted_output = emotion_detector(response_text)
print(json.dumps(formatted_output, indent=4))
