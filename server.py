"""
This module serves as the Flask server for emotion detection.
It integrates with Watson's emotion detection API and serves the analysis result to the client.
"""

from flask import Flask, render_template, request, jsonify
from emotion_detection import EmotionDetector  # Import EmotionDetector directly

app = Flask(__name__)

# Instantiate EmotionDetector
emotion_detector = EmotionDetector()


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handles emotion detection via POST request."""
    # Retrieve the text from the form data
    input_text = request.form.get('text', '').strip()  # Safely fetch and strip text input

    if not input_text:
        return jsonify({"error": "Input text cannot be empty!"}), 400  # Error for blank entries

    # Predict emotion using EmotionDetector
    result = emotion_detector.predict_emotion(input_text)

    if 'error' in result:  # Handle errors from prediction
        return jsonify(result), 400

    response_data = {
        "dominant_emotion": result["predicted_emotion"]
    }

    return jsonify(response_data), 200  # Return success response


@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')  # Render the home page


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
