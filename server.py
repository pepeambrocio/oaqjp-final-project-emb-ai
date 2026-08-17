"""
Server module for the Emotion Detection application.
Provides endpoints to analyze text and render the web interface.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Retrieves text from the request arguments, analyzes its emotion
    using the emotion_detector function, and returns a formatted string.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the detector function
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion to check for error states
    dominant_emotion = response['dominant_emotion']

    # Handle blank entries or invalid responses
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract values from the response dictionary for a valid run
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Return the exact string format requested by the customer
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main HTML template page for the user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost port 5000 (or 5001 if 5000 is busy)
    app.run(host="0.0.0.0", port=5000)
