from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_endpoint():
    # Get the 'text' parameter from the query string
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return "Error: No text provided for analysis.", 400

    # Call the emotion detection function
    try:
        result = emotion_detector(text_to_analyze)
    except Exception as e:
        return f"Error during emotion analysis: {str(e)}", 500

    # Format the response as requested
    response = (f"For the given statement, the system response is 'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
                f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}.")

    return response, 200

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
