import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

def emotion_detector(text_to_analyze):
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(URL, json = myobj, headers=headers) # Send a POST request to the API with the text and headers 

    # If the status code is 400, the input was blank/invalid: return all keys with None
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Change the format to a dictionary
    formatted_response = json.loads(response.text)

    # Extract the emotion block
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Score extraction
    anger_score   = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score    = emotions['fear']
    joy_score     = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }