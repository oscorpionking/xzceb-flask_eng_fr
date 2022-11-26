import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#authenticate

authenticator = IAMAuthenticator(apikey)

#setup service
language_t = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_t.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    french_text = language_t.translate(text=english_text, model_id='en-fr').get_result()
    print(french_text)
    return french_text['translations'][0]['translation']


english_to_french("Love")

def french_to_english(french_text):
    #write the code here
    english_text = language_t.translate(text=french_text, model_id='fr-en').get_result()
    #return frenchText
    print(english_text)
    return english_text['translations'][0]['translation']


french_to_english("bonjour")