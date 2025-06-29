import json
import requests

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=myobj, headers=header)
    if response.status_code == 400:
        emotion_dict= {}
        emotion_dict['anger'] = None
        emotion_dict['disgust'] = None
        emotion_dict['fear'] = None
        emotion_dict['joy'] = None
        emotion_dict['sadness'] = None
        emotion_dict['dominant_emotion'] = None

        return emotion_dict
    formatted_text = json.loads(response.text)
    emotion_dict = formatted_text['emotionPredictions'][0]['emotion']
    

    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict
