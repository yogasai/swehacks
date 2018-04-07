# # Using IBM Watson's Tone Analyzer to detect and interpret emotional, social, and writing cues found in text.
# # February 26, 2016
# # Version 1.0
 
# import requests
# import json
 
# def analyze_tone(text):
#     username = '5c2a9473-aeaf-4a32-a97d-24b898843c4f'
#     password = 'PN7c4sKsk0OD'
#     watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer-beta/api/v3/tone?version=2017-09-21'
#     headers = {"content-type": "application/json"}
#     data = text
#     try:
#         r = requests.post(watsonUrl, auth=(username,password),headers = headers,
#          data=data)
#         print(r.text)
#         return r.text
#     except:
#         return False

# def display_results(data):
#     data = json.loads(str(data))
#     print(data)
#     for i in data['document_tone']['tones']:
#         print(i['tone_name'])
#         print("-" * len(i['tone_name']))
#         for j in i['tones']:
#             print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
#         print()
#     print()
 
# def main():
     
#     data = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
#     if len(data) >= 1:
#         if data == 'q'.lower():
#             exit
#         results = analyze_tone(data)
#         if results != False:
#             display_results(results)
#             exit
#         else:
#             print("Something went wrong")
 
# main()

import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version ='2017-09-21',
    username ='5c2a9473-aeaf-4a32-a97d-24b898843c4f',
    password ='PN7c4sKsk0OD'
)

text = 'Team, I know that times are tough! Product sales have been disappointing for the past three quarters. We have a competitive product, but we need to do a better job of selling it!'
content_type = 'application/json'

tone = tone_analyzer.tone({"text": text},content_type)

print(json.dumps(tone, indent=2))