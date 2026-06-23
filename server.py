"""Flask server that exposes the emotion detector as a web service."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask application
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """Receive the text from the interface, run emotion detection and format the response."""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    # If the dominant emotion is None, the input was invalid/blank
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the index HTML page that serves as the user interface."""
    return render_template('index.html')


if __name__ == "__main__":
    # Deploy the application on localhost, port 5000
    app.run(host="0.0.0.0", port=5000)
