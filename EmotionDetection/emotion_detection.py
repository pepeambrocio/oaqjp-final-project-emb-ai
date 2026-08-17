import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers) 
    formatted_response = json.loads(response.text)

    # 1. Extract the actual dictionary of emotion scores
    # Watson path: emotionPredictions -> first item -> emotion
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # 2. Find the key with the maximum value
    max_emotion = max(emotions, key=emotions.get)

    # 3. Print using the correct variable
    print(f"Max emotion: {max_emotion} ({emotions[max_emotion]})")

    return max_emotion
