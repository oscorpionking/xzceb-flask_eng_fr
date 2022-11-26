import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#authenticate

authenticator = IAMAuthenticator(apikey)

#setup service
language_t = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_t.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    frenchText = language_t.translate(text=englishText, model_id='en-fr').get_result()
    print(frenchText)
    return frenchText['translations'][0]['translation']
    

englishToFrench("Love")

def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_t.translate(text=frenchText, model_id='fr-en').get_result()
    #return frenchText
    print(englishText)
    return englishText['translations'][0]['translation']
frenchToEnglish("bonjour")