from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='0809098e-e8db-4891-bc00-1648586b9a7e',
    password='reJC1vsBSdVf',
    x_watson_learning_opt_out=False
)


def transcribe(audioFile, contentType):
	with open(join(dirname(__file__), audioFile), 'rb') as audio_file:
		json_result = speech_to_text.recognize(
	        audio_file, 
	        content_type=contentType, 
	        timestamps=False,
	        word_confidence=False)

		return json_result["results"][0]["alternatives"][0]["transcript"]

result = transcribe('./audio2.wav', 'audio/wav')

print(result)

