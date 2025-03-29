"""
This module serves as the Flask server for emotion detection.
It integrates with Watson's emotion detection API and serves the analysis result to the client.
"""

from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector  # Import the function

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handles emotion detection via POST request."""
    # Retrieve the text from the form data
    input_text = request.form.get('text', '').strip()  # Safely fetch and strip text input

    if not input_text:
        return jsonify({"error": "Input text cannot be empty!"}), 400  # Error for blank entries

    # Example response from IBM Watson for testing purposes
    # Replace this with an actual API call to get the response text
    response_text = '{"anger": 0.1, "disgust": 0.05, "fear": 0.2, "joy": 0.7, "sadness": 0.15}'
    
    # Use the emotion_detector function to get the result
    result = emotion_detector(response_text)

    if 'error' in result:
        return jsonify(result), 400

    response_data = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }

    return jsonify(response_data), 200  # Return success response

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')  # Render the home page

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
