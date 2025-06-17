"""Emotion Detector Flask App
This module provides a web interface for emotion detection using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the emotions in the provided text and return the results."""
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None:
        return {"error": "invalid/ or no data recieved"}
    returned_dict = emotion_detector(text_to_analyze)
    if returned_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger' : {returned_dict['anger']}, "
        f"'disgust' : {returned_dict['disgust']}, "
        f"'fear' : {returned_dict['fear']}, "
        f"'joy' : {returned_dict['joy']}, "
        f"'sadness' : {returned_dict['sadness']}. "
        f"The dominant emotion is {returned_dict['dominant_emotion']}"
    ), 200

@app.route('/')
def index_html_renderer():
    """Render the index HTML page."""
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host = 'localhost', port=5000)
